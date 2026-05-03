# InstaGuard: Fake Profile Detector 

Have you ever wondered if an Instagram account is a real person or just a bot? **InstaGuard** uses Artificial Intelligence to figure it out for you!

This project looks at simple details from a profile (like how many followers they have, if they have a profile picture, and their username) and predicts if the account is fake or real with over 90% accuracy.

## What does it do?
- **Easy to Use:** Just type in the profile details on our beautiful web page.
- **Smart AI:** It automatically does the math to find suspicious patterns (like having 5,000 follows but 0 posts).
- **Fast Results:** It gives you an instant verdict: "**Looks Legit!**" or "**Looks like a Bot!**"
demovideo: 
https://github.com/yashwanth2202/Fake_profile_detector/raw/main/assets/demo.mp4

---

## How to Run the App on Your Computer

It is incredibly easy to start the app yourself! Just follow these 3 simple steps:

### Step 1: Download the Project
Download or clone this project to your computer.
```bash
git clone https://github.com/yashwanth2202/Fake_profile_detector.git
cd Fake_profile_detector
```

### Step 2: Install the Requirements
You need to install the AI tools (like Pandas and Flask) so the code can run. Run this command in your terminal:
```bash
pip install -r requirements.txt
```

### Step 3: Start the Website!
Start the web server by running:
```bash
python app.py
```
That's it! Now open your web browser (like Chrome or Safari) and go to this link:
 **http://127.0.0.1:5000**

---

## (Optional) For Developers
If you want to look under the hood and re-train the AI model yourself, you can run the main pipeline script:
```bash
python main.py
```
This will load the raw data, train the AI, and print out a detailed accuracy report in your terminal!
