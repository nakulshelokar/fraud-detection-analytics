import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Fraud Detection Analytics",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 Fraud Detection Analytics")
st.write("Interactive dashboard for analyzing suspicious financial transactions.")

# Load data
df = pd.read_csv("data/transactions.csv")

# Metrics
total_transactions = len(df)
fraud_transactions = int(df["Is_Fraud"].sum())
legitimate_transactions = total_transactions - fraud_transactions
fraud_rate = (fraud_transactions / total_transactions) * 100
fraud_amount = df.loc[df["Is_Fraud"] == 1, "Amount"].sum()

# KPI cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Transactions", total_transactions)
col2.metric("Fraud Transactions", fraud_transactions)
col3.metric("Fraud Rate", f"{fraud_rate:.2f}%")
col4.metric("Fraud Amount", f"₹{fraud_amount:,.0f}")

st.divider()

# Fraud distribution
fraud_data = (
    df["Is_Fraud"]
    .value_counts()
    .rename(index={0: "Legitimate", 1: "Fraud"})
    .reset_index()
)

fraud_data.columns = ["Transaction Status", "Count"]

fig_fraud = px.pie(
    fraud_data,
    names="Transaction Status",
    values="Count",
    title="Fraud vs Legitimate Transactions"
)

st.plotly_chart(fig_fraud, use_container_width=True)

# Fraud by location
location_data = (
    df.groupby("Location", as_index=False)["Is_Fraud"]
    .sum()
    .sort_values("Is_Fraud", ascending=False)
)

location_data.columns = ["Location", "Fraud Transactions"]

fig_location = px.bar(
    location_data,
    x="Location",
    y="Fraud Transactions",
    title="Fraud Transactions by Location"
)

st.plotly_chart(fig_location, use_container_width=True)

# Fraud by device
device_data = (
    df.groupby("Device_Type", as_index=False)["Is_Fraud"]
    .sum()
)

device_data.columns = ["Device Type", "Fraud Transactions"]

fig_device = px.bar(
    device_data,
    x="Device Type",
    y="Fraud Transactions",
    title="Fraud Transactions by Device Type"
)

st.plotly_chart(fig_device, use_container_width=True)

# Suspicious transactions
st.subheader("🚨 Suspicious Transactions")

suspicious = df[df["Is_Fraud"] == 1]

st.dataframe(
    suspicious,
    use_container_width=True
)

st.warning(
    f"Detected {fraud_transactions} potentially fraudulent transactions "
    f"with a total value of ₹{fraud_amount:,.0f}."
)
