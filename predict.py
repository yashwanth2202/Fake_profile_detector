import config
from src.predictor import load_model, predict_profile

def get_user_input():
    print("\n--- Instagram Profile Analyzer ---")
    print("Please enter the following profile stats to detect if it is real or fake.\n")
    
    try:
        features = {
            'profile pic': int(input("Has Profile Picture? (1 for Yes, 0 for No): ")),
            'nums/length username': float(input("Ratio of numbers to length in username (e.g., 0.27 or 0.0): ")),
            'fullname words': int(input("Number of words in full name (e.g., 2): ")),
            'nums/length fullname': float(input("Ratio of numbers to length in full name (e.g., 0.0): ")),
            'name==username': int(input("Is full name exactly the same as username? (1 for Yes, 0 for No): ")),
            'description length': int(input("Number of characters in bio/description: ")),
            'external URL': int(input("Has an external URL in bio? (1 for Yes, 0 for No): ")),
            'private': int(input("Is the account private? (1 for Yes, 0 for No): ")),
            '#posts': int(input("Number of posts: ")),
            '#followers': int(input("Number of followers: ")),
            '#follows': int(input("Number of accounts they follow: "))
        }
        return features
    except ValueError:
        print("\nError: Invalid input. Please enter numbers only where required.")
        return None

def main():
    print("Loading AI Model...")
    try:
        model = load_model(config.MODEL_SAVE_PATH)
    except FileNotFoundError:
        print(f"Error: Could not find model at {config.MODEL_SAVE_PATH}. Please run main.py first to train it.")
        return
        
    while True:
        features = get_user_input()
        if features:
            print("\nAnalyzing profile...")
            result = predict_profile(model, features)
            
            print("\n===============================")
            if result == "Fake":
                print("!!! VERDICT: FAKE PROFILE !!!")
            else:
                print("*** VERDICT: REAL PROFILE ***")
            print("===============================\n")
            
        again = input("Analyze another profile? (y/n): ")
        if again.lower() != 'y':
            break

if __name__ == "__main__":
    main()
