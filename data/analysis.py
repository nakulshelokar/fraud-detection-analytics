import pandas as pd


df = pd.read_csv("data/transactions.csv")

total_transactions = len(df)
fraud_transactions = df["Is_Fraud"].sum()
legitimate_transactions = total_transactions - fraud_transactions

fraud_rate = (fraud_transactions / total_transactions) * 100
total_transaction_amount = df["Amount"].sum()
fraud_amount = df.loc[df["Is_Fraud"] == 1, "Amount"].sum()

print("===== FRAUD DETECTION ANALYTICS =====")

print(f"Total Transactions: {total_transactions}")
print(f"Fraudulent Transactions: {fraud_transactions}")
print(f"Legitimate Transactions: {legitimate_transactions}")
print(f"Fraud Rate: {fraud_rate:.2f}%")
print(f"Total Transaction Amount: ₹{total_transaction_amount:,.0f}")
print(f"Amount Involved in Fraud: ₹{fraud_amount:,.0f}")

print("\nFraud by Location:")
print(
    df.groupby("Location")["Is_Fraud"]
    .sum()
    .sort_values(ascending=False)
)

print("\nFraud by Device Type:")
print(
    df.groupby("Device_Type")["Is_Fraud"]
    .sum()
    .sort_values(ascending=False)
)

print("\nAverage Transaction Amount:")
print(f"₹{df['Amount'].mean():,.2f}")
