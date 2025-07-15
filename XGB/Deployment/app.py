import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json

# Load model and scaler
@st.cache_resource
def load_model_and_scaler():
    model = joblib.load(r"E:\Assignment\Zeru_assign\XGB\xgb_wallet_model.pkl")
    scaler = joblib.load(r"E:\Assignment\Zeru_assign\XGB\scaler.pkl")
    return model, scaler

def preprocess(df):
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
    def normalize_usd(row):
        try:
            return float(row["actionData.amount"]) * float(row["actionData.assetPriceUSD"])
        except:
            return 0.0
    df["usd_value"] = df.apply(normalize_usd, axis=1)
    df["action"] = df["action"].str.lower()
    return df

def feature_engineering(df):
    wallet_df = df.groupby("userWallet").agg(
        tx_count=("txHash", "count"),
        total_usd=("usd_value", "sum"),
        unique_actions=("action", "nunique"),
        deposit_total=("usd_value", lambda x: x[df["action"] == "deposit"].sum()),
        borrow_total=("usd_value", lambda x: x[df["action"] == "borrow"].sum()),
        repay_total=("usd_value", lambda x: x[df["action"] == "repay"].sum()),
        liquidation_count=("action", lambda x: (x == "liquidationcall").sum()),
        first_tx=("timestamp", "min"),
        last_tx=("timestamp", "max"),
    )
    wallet_df["days_active"] = (wallet_df["last_tx"] - wallet_df["first_tx"]).dt.days + 1
    wallet_df["loan_to_value"] = wallet_df["borrow_total"] / (wallet_df["deposit_total"] + 1)
    wallet_df["repay_ratio"] = wallet_df["repay_total"] / (wallet_df["borrow_total"] + 1)
    return wallet_df.reset_index()

st.title("Wallet Credit Score Prediction (XGBoost Model)")

st.write("Upload your wallet transactions JSON file to get credit scores for each wallet.")

uploaded_file = st.file_uploader("Choose a JSON file", type="json")

if uploaded_file is not None:
    try:
        data = json.load(uploaded_file)
        df = pd.json_normalize(data)
        df = preprocess(df)
        features = feature_engineering(df)

        feature_cols = [
            "tx_count",
            "total_usd",
            "unique_actions",
            "deposit_total",
            "borrow_total",
            "repay_total",
            "liquidation_count",
            "days_active",
            "loan_to_value",
            "repay_ratio",
        ]
        X = features[feature_cols].fillna(0)

        model, scaler = load_model_and_scaler()
        X_scaled = scaler.transform(X)
        predictions = model.predict(X_scaled)
        features["predicted_score"] = predictions.clip(0, 1000).round(2)

        st.success("Prediction complete! See results below.")
        st.dataframe(features[["userWallet", "predicted_score"]])

        st.download_button(
            label="Download Scores as CSV",
            data=features[["userWallet", "predicted_score"]].to_csv(index=False),
            file_name="wallet_scores.csv",
            mime="text/csv"
        )
    except Exception as e:
        st.error(f"Error processing file: {e}")
else:
    st.info("Please upload a JSON file to begin.")