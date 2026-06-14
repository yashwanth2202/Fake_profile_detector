import streamlit as st
import os
import config
from src.predictor import load_model, predict_profile

# Set page configuration with a premium look and feel
st.set_page_config(
    page_title="Fake Profile Detector",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom styles for a modern, glassmorphic UI look
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #1e1e2f 0%, #11111d 100%);
        color: #ffffff;
    }
    .stApp {
        background-color: #0e1117;
    }
    .title-container {
        text-align: center;
        padding: 2rem 0;
    }
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(90deg, #ff8a00, #e52e71);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #a0aec0;
    }
    .feature-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 1rem;
    }
    .real-result {
        background-color: rgba(46, 204, 113, 0.15);
        border: 2px solid #2ecc71;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
    }
    .fake-result {
        background-color: rgba(231, 76, 60, 0.15);
        border: 2px solid #e74c3c;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# App header
st.markdown('<div class="title-container"><h1 class="main-title">🛡️ Instagram Fake Profile Detector</h1><p class="subtitle">Enter the profile details below to verify if it\'s authentic or fake.</p></div>', unsafe_allow_html=True)

# Cache model loading for performance
@st.cache_resource
def get_model():
    model_path = config.MODEL_SAVE_PATH
    if not os.path.exists(model_path):
        return None
    return load_model(model_path)

model = get_model()

if model is None:
    st.error("⚠️ Trained model file not found. Please run the training pipeline first (e.g., run `python main.py`).")
else:
    # Form container
    with st.form("detector_form"):
        st.markdown("### 📝 Profile Attributes")
        
        col1, col2 = st.columns(2)
        
        with col1:
            username = st.text_input("Username", placeholder="e.g., john_doe123")
            fullname = st.text_input("Full Name", placeholder="e.g., John Doe")
            bio = st.text_area("Bio / Description", placeholder="e.g., Traveller | Tech enthusiast | Coffee lover")
            
            posts = st.number_input("Number of Posts", min_value=0, step=1, value=0)
            
        with col2:
            followers = st.number_input("Number of Followers", min_value=0, step=1, value=0)
            follows = st.number_input("Number of Followings", min_value=0, step=1, value=0)
            
            has_profile_pic = st.selectbox("Has Profile Picture?", ["Yes", "No"])
            has_external_url = st.selectbox("Has External Link in Bio?", ["No", "Yes"])
            is_private = st.selectbox("Is Account Private?", ["No", "Yes"])
            
        submitted = st.form_submit_button("🔍 Analyze Profile")
        
    if submitted:
        # Preprocessing & Feature Engineering
        def count_numbers_ratio(text):
            if not text:
                return 0.0
            num_count = sum(c.isdigit() for c in text)
            return num_count / len(text)
            
        nums_length_username = count_numbers_ratio(username)
        nums_length_fullname = count_numbers_ratio(fullname)
        
        fullname_words = len(fullname.split()) if fullname else 0
        name_equals_username = 1 if (username and username.lower() == fullname.lower()) else 0
        description_length = len(bio)
        
        features = {
            'profile pic': 1 if has_profile_pic == "Yes" else 0,
            'nums/length username': nums_length_username,
            'fullname words': fullname_words,
            'nums/length fullname': nums_length_fullname,
            'name==username': name_equals_username,
            'description length': description_length,
            'external URL': 1 if has_external_url == "Yes" else 0,
            'private': 1 if is_private == "Yes" else 0,
            '#posts': posts,
            '#followers': followers,
            '#follows': follows
        }
        
        with st.spinner("Analyzing profile attributes..."):
            result = predict_profile(model, features)
            
        st.markdown("---")
        st.markdown("### 📊 Prediction Result")
        
        if result == "Real":
            st.markdown(
                f"""
                <div class="real-result">
                    <h2 style="color: #2ecc71; margin: 0;">✅ Legitimate Profile</h2>
                    <p style="margin: 0.5rem 0 0 0; color: #a0aec0;">Our model predicts this account is <strong>Real</strong>.</p>
                </div>
                """, 
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div class="fake-result">
                    <h2 style="color: #e74c3c; margin: 0;">🚨 Suspicious Profile</h2>
                    <p style="margin: 0.5rem 0 0 0; color: #a0aec0;">Our model predicts this account is <strong>Fake</strong>.</p>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
        # Display the calculated features for transparency
        with st.expander("🔍 View Extracted Features"):
            st.json(features)
