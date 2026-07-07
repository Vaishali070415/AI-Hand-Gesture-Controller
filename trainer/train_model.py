'''''
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_csv("Dataset/gestures.csv")
#print(df["label"].value_counts())

# Features and Labels
X = df.drop("label", axis=1)
y = df["label"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy*100:.2f}%")

# Save Model
joblib.dump(model, "models/gesture_model.pkl")

print("Model Saved Successfully!")
'''''
import os 
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# ===============================
# Load Dataset
# ===============================

dataset_path = "Dataset/gestures.csv"

if not os.path.exists(dataset_path):
    print("Dataset not found!")
    exit()

df = pd.read_csv(dataset_path)

# ===============================
# Check Dataset
# ===============================

print("\nDataset Summary:\n")
print(df["label"].value_counts())

# ===============================
# Features and Labels
# ===============================

X = df.drop("label", axis=1)
y = df["label"]

# ===============================
# Train Test Split
# ===============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ===============================
# Random Forest Model
# ===============================

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42
)

model.fit(X_train, y_train)

# ===============================
# Prediction
# ===============================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\n==============================")
print(f"Accuracy : {accuracy*100:.2f}%")
print("==============================\n")

print(classification_report(y_test, y_pred))

# ===============================
# Save Model
# ===============================

os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/gesture_model.pkl")

print("Model Saved Successfully!")