# XGBoost Wallet Credit Model

This project builds a credit scoring model for blockchain wallets using transaction data and XGBoost regression. The workflow includes data loading, preprocessing, feature engineering, model training, and evaluation.

## Features

- Loads and normalizes JSON transaction data
- Preprocesses timestamps and computes USD values
- Aggregates wallet-level features (transaction count, total USD, unique actions, etc.)
- Simulates a credit score for demonstration
- Trains an XGBoost regressor
- Evaluates with RMSE and MAPE
- Saves the trained model and scaler

## Usage

1. **Install requirements**  
   Make sure you have the following Python packages:
   - pandas
   - numpy
   - xgboost
   - scikit-learn
   - joblib

   You can install them with:
   ```sh
   pip install pandas numpy xgboost scikit-learn joblib
   ```

2. **Prepare your data**  
   Place your JSON file at:
   ```
   E:\Assignment\Zeru_assign\user-wallet-transactions.json\user-wallet-transactions.json
   ```
   or update the `json_path` variable in the script.

3. **Run the script**  
   ```sh
   python xgb.py
   ```

## Main Functions

- **load_data(json_path):** Loads and normalizes JSON data into a DataFrame.
- **preprocess(df):** Parses timestamps and computes USD values.
- **feature_engineering(df):** Aggregates wallet-level features and simulates a target score.
- **train_model(df):** Trains an XGBoost regressor, prints RMSE and MAPE, and saves the model and scaler.

## Output

- Prints model evaluation metrics:
  ```
  Model Trained | RMSE: XX.XX | MAPE: XX.XX%
  Model and Scaler saved.
  Script completed successfully.
  ```
- Saves:
  - `xgb_wallet_model.pkl` (trained model)
  - `scaler.pkl` (feature scaler)

## Notes

- The target `score` is simulated for demonstration. Replace with your real target if available.
- High MAPE values may indicate zeros in the target variable; filter or handle accordingly.
- You can extend feature engineering as needed for your use case.

---
