import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
import joblib

# Load dataset
df = pd.read_csv("heart.csv")

# Confirm 'condition' exists
if 'condition' not in df.columns:
    raise ValueError("Expected 'condition' column as target.")

# Convert 'condition' to binary target
df['target'] = df['condition'].apply(lambda x: 1 if x > 0 else 0)
df.drop(columns=['condition'], inplace=True)

# Split features and target
X = df.drop("target", axis=1)
y = df["target"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = GradientBoostingClassifier()
model.fit(X_train, y_train)

# Save model and metadata
joblib.dump(model, "model.pkl")
joblib.dump(X.columns.tolist(), "feature_columns.pkl")
joblib.dump(["No Disease", "Disease"], "target_names.pkl")

print("✅ Model trained and saved.")

