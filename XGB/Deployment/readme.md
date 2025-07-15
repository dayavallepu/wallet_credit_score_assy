# Wallet Credit Score Prediction (XGBoost Model) – Streamlit App

This Streamlit app allows you to upload a JSON file of wallet transactions and predicts credit scores for each wallet using a trained XGBoost model.

---

## Features

- Upload your wallet transaction JSON file.
- Automatic preprocessing and feature engineering.
- Predicts credit scores for each wallet.
- View results in the browser.
- Download the scores as a CSV file.

---

## How to Run

1. **Install requirements**

   Make sure you have Python 3.8+ installed.

   Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

2. **Model Files**

   Ensure the following files are present in the `XGB` directory:
   - `xgb_wallet_model.pkl`
   - `scaler.pkl`

3. **Start the Streamlit app**

   Open a terminal in the `XGB/Deployment` directory and run:
   ```sh
   streamlit run app.py
   ```

4. **Use the App**

   - Open the provided local URL in your browser.
   - Upload your wallet transactions JSON file.
   - View the predicted scores and download them as a CSV.

---

## Input Format

- The input should be a JSON file containing a list of wallet transaction records, with fields such as:
  - `userWallet`
  - `txHash`
  - `timestamp`
  - `action`
  - `actionData.amount`
  - `actionData.assetPriceUSD`
  - etc.

---

## Output

- The app displays a table of wallet addresses and their predicted credit scores.
- You can download the results as `wallet_scores.csv`.

---

## requirements.txt

```
streamlit==1.35.0
pandas==2.2.2
numpy==1.26.4
joblib==1.4.2
```

---

## Notes

- If you move the model or scaler files, update their paths in `app.py`.
- For best results, use the same data structure as used for model training.

---
```# Wallet Credit Score Prediction (XGBoost Model) – Streamlit App

This Streamlit app allows you to upload a JSON file of wallet transactions and predicts credit scores for each wallet using a trained XGBoost model.

---

## Features

- Upload your wallet transaction JSON file.
- Automatic preprocessing and feature engineering.
- Predicts credit scores for each wallet.
- View results in the browser.
- Download the scores as a CSV file.

---

## How to Run

1. **Install requirements**

   Make sure you have Python 3.8+ installed.

   Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

2. **Model Files**

   Ensure the following files are present in the `XGB` directory:
   - `xgb_wallet_model.pkl`
   - `scaler.pkl`

3. **Start the Streamlit app**

   Open a terminal in the `XGB/Deployment` directory and run:
   ```sh
   streamlit run app.py
   ```

4. **Use the App**

   - Open the provided local URL in your browser.
   - Upload your wallet transactions JSON file.
   - View the predicted scores and download them as a CSV.

---

## Input Format

- The input should be a JSON file containing a list of wallet transaction records, with fields such as:
  - `userWallet`
  - `txHash`
  - `timestamp`
  - `action`
  - `actionData.amount`
  - `actionData.assetPriceUSD`
  - etc.

---

## Output

- The app displays a table of wallet addresses and their predicted credit scores.
- You can download the results as `wallet_scores.csv`.

---

## requirements.txt

```
streamlit==1.35.0
pandas==2.2.2
numpy==1.26.4
joblib==1.4.2
```

---

## Notes

- If you move the model or scaler files, update their paths in `app.py`.
- For best results, use the same data structure as used for model