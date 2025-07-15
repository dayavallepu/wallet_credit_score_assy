# xgb_wallet_credit_model.py

import json # Load JSON data
import pandas as pd # Data manipulation and analysis
import numpy as np # Numerical operations
import xgboost as xgb # XGBoost library for gradient boosting
from sklearn.model_selection import train_test_split # Train-test split
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error # Evaluation metrics
from sklearn.preprocessing import MinMaxScaler # Feature scaling
import joblib # Model persistence


def load_data(json_path):
    """Load JSON data and normalize into a pandas DataFrame."""
    with open(json_path, "r") as f:
        data = json.load(f)
    return pd.json_normalize(data)


def preprocess(df):
    """Preprocess the DataFrame: parse timestamps and compute USD values."""
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")

    # Normalize amount to USD
    def normalize_usd(row):
        try:
            return float(row["actionData.amount"]) * float(row["actionData.assetPriceUSD"])
        except:
            return 0.0

    df["usd_value"] = df.apply(normalize_usd, axis=1)
    df["action"] = df["action"].str.lower()
    return df


def feature_engineering(df):
    """Aggregate wallet-level features and simulate a target score."""
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

    # Simulate target score for demo
    score = (
        300
        + 0.2 * wallet_df["deposit_total"]
        - 0.3 * wallet_df["liquidation_count"]
        + 100 * wallet_df["repay_ratio"]
        - 50 * wallet_df["loan_to_value"]
        + 0.5 * wallet_df["tx_count"]
    )
    wallet_df["score"] = score.clip(0, 1000)
    return wallet_df.reset_index()


def train_model(df):
    """Train an XGBoost regressor on wallet features and print evaluation metrics."""
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

    X = df[feature_cols].fillna(0)
    y = df["score"]

    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    model = xgb.XGBRegressor(
        objective="reg:squarederror", max_depth=4, n_estimators=100, learning_rate=0.1
    )
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    # Filter out zero targets for MAPE calculation
    nonzero_idx = y_test != 0
    mape = mean_absolute_percentage_error(y_test[nonzero_idx], y_pred[nonzero_idx]) * 100

    print(f"Model Trained | RMSE: {rmse:.2f} | MAPE: {mape:.2f}%")

    joblib.dump(model, "xgb_wallet_model.pkl")  # Save the trained model
    joblib.dump(scaler, "scaler.pkl")           # Save the scaler
    print("Model and Scaler saved.")

    return model


def main():
    json_path = r"E:\Assignment\Zeru_assign\user-wallet-transactions.json\user-wallet-transactions.json"  # change if needed
    df = load_data(json_path)                # Load the data from JSON file
    df = preprocess(df)                      # Preprocess the raw data
    features = feature_engineering(df)       # Generate wallet-level features
    train_model(features)                    # Train the model


if __name__ == "__main__":
    main()

print("✅ Script completed successfully.")

# printing predicted values for demonstration
# Model Trained | RMSE: 27.71 | MAPE: 0.18%
# Model and Scaler saved.