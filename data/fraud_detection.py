import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score


# Load transaction data
df = pd.read_csv("data/transactions.csv")

# Convert categorical columns into numerical values
df_encoded = pd.get_dummies(
    df,
    columns=["Transaction_Type", "Location", "Device_Type"],
    drop_first=True
)

# Separate features and target
X = df_encoded.drop(columns=["Transaction_ID", "Is_Fraud"])
y = df_encoded["Is_Fraud"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Display results
print("===== FRAUD DETECTION ANALYTICS =====")
print(f"Model Accuracy: {accuracy_score(y_test, predictions):.2%}")

print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Feature importance
feature_importance = pd.Series(
    model.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

print("\nMost Important Fraud Detection Features:")
print(feature_importance.head(10))
