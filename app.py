from flask import Flask, render_template, request, jsonify
import config
from src.predictor import load_model, predict_profile
import os

app = Flask(__name__)

# Load the model once when the server starts
try:
    model = load_model(config.MODEL_SAVE_PATH)
    print("Model loaded successfully!")
except FileNotFoundError:
    print("Error: Model not found. Run main.py to train it first.")
    model = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return jsonify({'error': 'Model not loaded'}), 500
        
    try:
        # Get JSON data from the request
        data = request.json
        
        # 1. Parse raw human inputs
        username = data.get('username', '')
        fullname = data.get('fullname', '')
        bio = data.get('bio', '')
        
        # 2. Automatically calculate complex ML features from raw strings
        def count_numbers_ratio(text):
            if not text: return 0.0
            num_count = sum(c.isdigit() for c in text)
            return num_count / len(text)
            
        nums_length_username = count_numbers_ratio(username)
        nums_length_fullname = count_numbers_ratio(fullname)
        
        fullname_words = len(fullname.split()) if fullname else 0
        name_equals_username = 1 if (username and username.lower() == fullname.lower()) else 0
        description_length = len(bio)
        
        # 3. Format all 11 features exactly as the model expects
        def safe_int(val, default=0):
            try:
                if val == "": return default
                return int(val)
            except (ValueError, TypeError):
                return default
                
        features = {
            'profile pic': safe_int(data.get('profile_pic', 0)),
            'nums/length username': nums_length_username,
            'fullname words': fullname_words,
            'nums/length fullname': nums_length_fullname,
            'name==username': name_equals_username,
            'description length': description_length,
            'external URL': safe_int(data.get('external_url', 0)),
            'private': safe_int(data.get('private', 0)),
            '#posts': safe_int(data.get('posts', 0)),
            '#followers': safe_int(data.get('followers', 0)),
            '#follows': safe_int(data.get('follows', 0))
        }
        
        # Make the prediction
        result = predict_profile(model, features)
        
        return jsonify({'result': result})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
