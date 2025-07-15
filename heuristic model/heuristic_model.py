import json
import pandas as pd
from datetime import datetime
import argparse
import os


def load_json(json_path):
    with open(json_path, "r") as f:
        data = json.load(f)
    return pd.json_normalize(data)


def preprocess(df):
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
    
    def to_usd(row):
        try:
            return float(row["actionData.amount"]) * float(row["actionData.assetPriceUSD"])
        except:
            return 0.0

    df["usd_value"] = df.apply(to_usd, axis=1)
    df["action"] = df["action"].str.lower()
    return df


def engineer_features(df):
    grouped = df.groupby("userWallet").agg(
        tx_count=("txHash", "count"),
        total_usd=("usd_value", "sum"),
        deposit_usd=("usd_value", lambda x: x[df["action"] == "deposit"].sum()),
        borrow_usd=("usd_value", lambda x: x[df["action"] == "borrow"].sum()),
        repay_usd=("usd_value", lambda x: x[df["action"] == "repay"].sum()),
        liquidation_count=("action", lambda x: (x == "liquidationcall").sum()),
        first_tx=("timestamp", "min"),
        last_tx=("timestamp", "max"),
        action_variety=("action", "nunique")
    )

    grouped["days_active"] = (grouped["last_tx"] - grouped["first_tx"]).dt.days + 1
    grouped["repay_ratio"] = grouped["repay_usd"] / (grouped["borrow_usd"] + 1)
    grouped["loan_to_value"] = grouped["borrow_usd"] / (grouped["deposit_usd"] + 1)

    return grouped.reset_index()


def score_wallets(df):
    def calculate_score(row):
        score = 400

        # Positive behaviors
        score += min(row["deposit_usd"] / 100, 200)       # Up to +200
        score += min(row["repay_ratio"] * 100, 150)       # Up to +150
        score += min(row["tx_count"] * 2, 100)            # Up to +100
        score += min(row["action_variety"] * 10, 50)      # +10 per unique action
        score += min(row["days_active"], 100)             # Max +100 for longevity

        # Negative behaviors
        score -= row["liquidation_count"] * 50            # -50 per liquidation
        score -= row["loan_to_value"] * 50                # Penalize high leverage

        return round(max(0, min(score, 1000)))            # Bound score between 0-1000

    df["credit_score"] = df.apply(calculate_score, axis=1)
    return df[["userWallet", "credit_score"]]


def save_scores(df, output_path="wallet_scores.json"):
    scores = dict(zip(df["userWallet"], df["credit_score"]))
    with open(output_path, "w") as f:
        json.dump(scores, f, indent=2)
    print(f"✅ Wallet scores saved to: {output_path}")


def main(json_file):
    raw = load_json(json_file)
    clean = preprocess(raw)
    features = engineer_features(clean)
    scored = score_wallets(features)
    save_scores(scored)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Heuristic Wallet Scoring")
    parser.add_argument("json_file", help="Path to JSON file")
    args = parser.parse_args()
    
    os.makedirs("output", exist_ok=True)
    main(args.json_file)


# example usage:
# python heuristic_model.py data/wallet_data.json