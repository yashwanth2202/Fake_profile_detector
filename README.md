# InstaGuard: Fake Profile Detector 🤖✨

InstaGuard is a full-stack Machine Learning application designed to detect fake or bot Instagram profiles with high accuracy. 

By analyzing raw profile metadata (such as follower ratios, bio length, and naming patterns), our custom XGBoost model can instantly determine whether an account is a real human or a bot.

## Features
- **High Accuracy AI:** Powered by an XGBoost Classifier trained on hundreds of real and fake profile data points, achieving ~91% accuracy.
- **Smart Feature Engineering:** Automatically extracts hidden patterns (like follower-to-following ratios and character composition) from raw human input.
- **Beautiful Web Interface:** A sleek, dark-mode glassmorphism frontend built with Vanilla CSS and HTML.
- **REST API:** A lightweight Flask backend that seamlessly bridges the Python AI model with the web interface.

## Technologies Used
- **Machine Learning:** `XGBoost`, `scikit-learn`, `pandas`
- **Backend:** `Python`, `Flask`
- **Frontend:** `HTML5`, `CSS3` (Vanilla/Glassmorphism), `JavaScript`

## How to Run the Project Locally

### 1. Setup the Environment
First, clone the repository and activate the virtual environment:
```bash
git clone https://github.com/yashwanth2202/Fake_profile_detector.git
cd Fake_profile_detector
.\venv\Scripts\activate
```

### 2. Install Dependencies
Make sure all required libraries are installed:
```bash
pip install -r requirements.txt
```

### 3. Run the Web Application
Start the Flask server to launch the web interface:
```bash
python app.py
```
Open your web browser and go to `http://127.0.0.1:5000` to interact with the AI!

### 4. (Optional) Re-Train the Model
If you want to view the evaluation metrics or re-train the XGBoost model from scratch, run the main pipeline script:
```bash
python main.py
```

## Project Structure
- `data/` - Contains the raw training dataset (`dataset.csv`).
- `models/` - Stores the compiled and serialized XGBoost model (`model.pkl`).
- `src/` - The core ML pipeline (data loaders, feature engineers, and predictors).
- `templates/` & `static/` - The HTML and CSS files for the frontend web interface.
- `app.py` - The Flask web server.
- `main.py` - The script to orchestrate the training pipeline.
