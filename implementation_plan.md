# Building the Fake Profile Detector (Step-by-Step)

Machine learning projects are like assembly lines. Data comes in at one end, it gets cleaned up, the model learns from it, and at the other end, we get predictions. We will build each station of this assembly line in the `src/` folder.

## User Review Required

Here is the roadmap we will follow:

### Step 1: Install Dependencies
We need special Python libraries to do machine learning.
#### [MODIFY] [requirements.txt](file:///d:/fake_profile_detector/requirements.txt)
- Add `pandas` (for managing data tables)
- Add `scikit-learn` (the standard library containing the Random Forest algorithm)
- We'll run `pip install -r requirements.txt` to install them.

---
### Step 2: Load the Data
We need a standardized way to pull data from our CSV file into our program.
#### [MODIFY] [src/data_loader.py](file:///d:/fake_profile_detector/src/data_loader.py)
- We will write a simple function called `load_data()` that reads `dataset.csv` using the paths we defined in `config.py`.

---
### Step 3: Prepare the Data (Preprocessing & Splitting)
A machine learning model is like a student. It needs practice problems (training data) and a final exam (testing data) to see if it actually learned.
#### [MODIFY] [src/preprocessor.py](file:///d:/fake_profile_detector/src/preprocessor.py)
- We will write a function to split our dataset. 80% of the data will be used to train the model, and 20% will be hidden away to test it later.

---
### Step 4: Train the Model
This is where the magic happens. We teach the model what a "fake profile" looks like.
#### [MODIFY] [src/model_trainer.py](file:///d:/fake_profile_detector/src/model_trainer.py)
- We will build a Random Forest Classifier.
- We will feed it our 80% training data so it can learn the patterns (e.g., "if they have 0 followers and 5000 follows, they are probably fake").
- We will save the trained model to the `models/` folder.

---
### Step 5: Test & Evaluate
We need to know if the model is actually good.
#### [MODIFY] [src/visualiser.py](file:///d:/fake_profile_detector/src/visualiser.py)
- We will make the model predict the 20% test data we hid earlier.
- We will compare its predictions to the real answers to calculate its **Accuracy** (how often it's right).

---
### Step 6: Putting it all together
We will connect all these pieces in `main.py` so the whole pipeline runs smoothly from start to finish.
#### [MODIFY] [main.py](file:///d:/fake_profile_detector/main.py)
- Update it to run the data loader -> preprocessor -> trainer -> evaluator sequence.

## Verification Plan
1. We will run `python main.py` at the end of the process.
2. If successful, we should see an accuracy score printed in the terminal (e.g., "Accuracy: 92%").
3. We should see a new file called `model.pkl` appear in the `models/` folder.
