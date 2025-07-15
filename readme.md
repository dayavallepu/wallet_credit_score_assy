# Zeru Assign – Blockchain Wallet Credit Analysis

This repository contains code and notebooks for analyzing blockchain wallet transaction data, performing exploratory data analysis (EDA), and building both heuristic and machine learning-based wallet credit scoring models.

---

## Project Structure

```
Zeru_assign/
│
├── EDA.ipynb                # Exploratory Data Analysis notebook
│
├── heuristic model/
│   └── heuristic_model.py   # Heuristic scoring script
│
├── XGB/
│   ├── xgb.py               # XGBoost-based credit scoring script
│   ├── xgb_wallet_model.pkl # Trained XGBoost model
│   ├── scaler.pkl           # Feature scaler for XGBoost model
│   └── Deployment/
│       └── app.py           # Streamlit app for XGBoost model
│
├── data/
│   └── user-wallet-transactions.json # Example input data
│
├── requirements.txt         # Python dependencies
├── analysis.md              # EDA and insights summary
└── README.md                # Project overview and instructions
```

---

## Features

- **EDA:** Visualizes missing values, action distributions, transaction values, and wallet activity.
- **Heuristic Model:** Assigns interpretable credit scores to wallets based on transaction behaviors.
- **XGBoost Model:** Trains a machine learning model for wallet credit scoring using engineered features.
- **Streamlit App:** Upload a JSON file and get wallet credit scores instantly via a web interface.

---

## Setup

1. **Clone the repository**
   ```sh
   git clone <repo-url>
   cd Zeru_assign
   ```

2. **Install requirements**
   ```sh
   pip install -r requirements.txt
   ```

3. **Prepare your data**
   - Place your wallet transaction JSON file in the `data/` folder or update the script paths as needed.

---

## How to Run

### 1. Exploratory Data Analysis

Open and run `EDA.ipynb` in Jupyter or VS Code to explore the data and visualize key patterns.

---

### 2. Heuristic Model

Assigns scores based on wallet behaviors.

```sh
python heuristic model/heuristic_model.py data/user-wallet-transactions.json
```

- Outputs: `wallet_scores.json` with wallet addresses and their heuristic credit scores.

---

### 3. XGBoost Model

Trains and evaluates a machine learning model for credit scoring.

```sh
python XGB/xgb.py
```

- Outputs: `xgb_wallet_model.pkl` and `scaler.pkl` for deployment.

---

### 4. Streamlit Web App

Upload a JSON file and get wallet credit scores in your browser.

```sh
cd XGB/Deployment
streamlit run app.py
```

- Open the provided local URL, upload your JSON file, and download the results as CSV.

---

## requirements.txt

```
pandas==2.2.2
numpy==1.26.4
xgboost==2.0.3
scikit-learn==1.4.2
joblib==1.4.2
streamlit==1.35.0
```

---

## Analysis & Insights

See [analysis.md](analysis.md) for a summary of data quality, user behaviors, and scoring logic.

---

## Notes

- The XGBoost model uses simulated scores for demonstration. Replace with real targets if available.
- For best results, ensure your input JSON matches the expected schema.
- You can extend feature engineering and scoring logic as needed for your use case.

---

## License

MIT License

---
```# Zeru Assign – Blockchain Wallet Credit Analysis

This repository contains code and notebooks for analyzing blockchain wallet transaction data, performing exploratory data analysis (EDA), and building both heuristic and machine learning-based wallet credit scoring models.

---

## Project Structure

```
Zeru_assign/
│
├── EDA.ipynb                # Exploratory Data Analysis notebook
│
├── heuristic model/
│   └── heuristic_model.py   # Heuristic scoring script
│
├── XGB/
│   ├── xgb.py               # XGBoost-based credit scoring script
│   ├── xgb_wallet_model.pkl # Trained XGBoost model
│   ├── scaler.pkl           # Feature scaler for XGBoost model
│   └── Deployment/
│       └── app.py           # Streamlit app for XGBoost model
│
├── data/
│   └── user-wallet-transactions.json # Example input data
│
├── requirements.txt         # Python dependencies
├── analysis.md              # EDA and insights summary
└── README.md                # Project overview and instructions
```

---

## Features

- **EDA:** Visualizes missing values, action distributions, transaction values, and wallet activity.
- **Heuristic Model:** Assigns interpretable credit scores to wallets based on transaction behaviors.
- **XGBoost Model:** Trains a machine learning model for wallet credit scoring using engineered features.
- **Streamlit App:** Upload a JSON file and get wallet credit scores instantly via a web interface.

---

## Setup

1. **Clone the repository**
   ```sh
   git clone <repo-url>
   cd Zeru_assign
   ```

2. **Install requirements**
   ```sh
   pip install -r requirements.txt
   ```

3. **Prepare your data**
   - Place your wallet transaction JSON file in the `data/` folder or update the script paths as needed.

---

## How to Run

### 1. Exploratory Data Analysis

Open and run `EDA.ipynb` in Jupyter or VS Code to explore the data and visualize key patterns.

---

### 2. Heuristic Model

Assigns scores based on wallet behaviors.

```sh
python heuristic model/heuristic_model.py data/user-wallet-transactions.json
```

- Outputs: `wallet_scores.json` with wallet addresses and their heuristic credit scores.

---

### 3. XGBoost Model

Trains and evaluates a machine learning model for credit scoring.

```sh
python XGB/xgb.py
```

- Outputs: `xgb_wallet_model.pkl` and `scaler.pkl` for deployment.

---

### 4. Streamlit Web App

Upload a JSON file and get wallet credit scores in your browser.

```sh
cd XGB/Deployment
streamlit run app.py
```

- Open the provided local URL, upload your JSON file, and download the results as CSV.

---

## requirements.txt

```
pandas==2.2.2
numpy==1.26.4
xgboost==2.0.3
scikit-learn==1.4.2
joblib==1.4.2
streamlit==1.35.0
```

---

## Analysis & Insights

See [analysis.md](analysis.md) for a summary of data quality, user behaviors, and scoring logic.

---

## Notes

- The XGBoost model uses simulated scores for demonstration. Replace with real targets if available.
- For best results, ensure your input JSON matches the expected schema.
- You can extend feature engineering and scoring logic as needed for your use case.

---

## License