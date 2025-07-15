# Heuristic Wallet Credit Scoring

This project provides a simple, interpretable heuristic model to assign credit scores to blockchain wallets based on their transaction history.

## Features

- Loads and normalizes JSON transaction data
- Preprocesses timestamps and computes USD values
- Aggregates wallet-level features (transaction count, total USD, deposits, borrows, repayments, etc.)
- Assigns a credit score (0-1000) to each wallet based on positive and negative behaviors
- Saves the scores as a JSON file

## How It Works

1. **Load Data:** Reads a JSON file containing wallet transaction data.
2. **Preprocess:** Converts timestamps and calculates USD value for each transaction.
3. **Feature Engineering:** Aggregates wallet-level statistics (deposits, borrows, repayments, liquidations, etc.).
4. **Scoring:** Applies a transparent heuristic to assign a credit score to each wallet.
5. **Save Scores:** Outputs a JSON file mapping wallet addresses to their credit scores.

## How to Run

1. **Install requirements**

   ```sh
   pip install -r requirements.txt
   ```

2. **Prepare your data**

   - Place your wallet transaction JSON file somewhere accessible (e.g., `data/wallet_data.json`).

3. **Run the script**

   ```sh
   python heuristic_model.py path/to/your/wallet_data.json
   ```

   - The script will output a file named `wallet_scores.json` in the current directory.
   - If you run from the project root, you can use:
     ```sh
     python heuristic_model.py data/wallet_data.json
     ```

4. **Output**

   - The resulting `wallet_scores.json` will contain a mapping of wallet addresses to their credit scores, e.g.:
     ```json
     {
       "0x123...": 750,
       "0xabc...": 420
     }
     ```

## Scoring Logic

- **Positive behaviors:**
  - Large deposits, high repayment ratio, more transactions, diverse actions, and longer activity increase the score.
- **Negative behaviors:**
  - Liquidations and high leverage (loan-to-value) decrease the score.
- **Score is bounded between 0 and 1000.**

## requirements.txt

See below for the required packages and versions.

---
