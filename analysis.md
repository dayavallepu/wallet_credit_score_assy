# Data Analysis Summary

This document summarizes the exploratory data analysis (EDA) and heuristic scoring logic applied to the wallet transaction dataset.

---

## 1. Missing Values Analysis

- **Most columns** (e.g., `userWallet`, `network`, `protocol`, `txHash`, etc.) have **no missing values**.
- **Some columns** (e.g., `actionData.toId`, `actionData.borrowRateMode`, `actionData.liquidatorId`, etc.) have **many missing values**.  
  These fields are only relevant for certain transaction types or actions.
- **Columns with a high number of missing values** may need to be dropped, imputed, or handled carefully in further analysis or modeling.

---

## 2. Action Distribution

- The action frequency plot shows which transaction types are most common in the dataset.
- **Deposit** and **redeemunderlying** are the most frequent actions, followed by **borrow** and **repay**.
- **Liquidationcall** is rare, indicating few wallets are liquidated.

---

## 3. Transaction Value Distribution

- The USD value histogram (log scale, colorful) reveals the distribution of transaction sizes.
- **Most transactions are of small value**, with a long tail of larger transactions.
- Outliers or extremely large transactions are easily visible.

---

## 4. Wallet Activity Distribution

- The wallet activity histogram (log scale, colorful) shows how many transactions each wallet has performed.
- **Most wallets are low-activity** (few transactions), while a small number of wallets are highly active.
- This highlights user engagement and possible power users or bots.

---

## 5. Wallet Summary Statistics

- For each wallet, features such as transaction count, total USD value, unique actions, deposit/borrow/repay totals, liquidation count, days active, loan-to-value, and repay ratio are computed.
- These features are used for both EDA and scoring.

---

## 6. Heuristic Credit Scoring Logic

- **Positive behaviors** (increase score):
  - Large deposits
  - High repayment ratio
  - More transactions
  - Diverse actions
  - Longer activity period
- **Negative behaviors** (decrease score):
  - Liquidations
  - High leverage (loan-to-value)
- **Score is bounded between 0 and 1000.**
- Scores are saved as a JSON mapping of wallet addresses to their credit scores.

---

## 7. Insights

- The dataset is generally clean, but some columns are sparse and should be handled with care.
- Most users interact with the protocol in simple ways (deposit/withdraw), while a few are highly active or take on more risk (borrow/repay/liquidate).
- The scoring system rewards responsible and diverse activity, while penalizing risky or negative behaviors.

---
```# Data Analysis Summary

This document summarizes the exploratory data analysis (EDA) and heuristic scoring logic applied to the wallet transaction dataset.

---

## 1. Missing Values Analysis

- **Most columns** (e.g., `userWallet`, `network`, `protocol`, `txHash`, etc.) have **no missing values**.
- **Some columns** (e.g., `actionData.toId`, `actionData.borrowRateMode`, `actionData.liquidatorId`, etc.) have **many missing values**.  
  These fields are only relevant for certain transaction types or actions.
- **Columns with a high number of missing values** may need to be dropped, imputed, or handled carefully in further analysis or modeling.

---

## 2. Action Distribution

- The action frequency plot shows which transaction types are most common in the dataset.
- **Deposit** and **redeemunderlying** are the most frequent actions, followed by **borrow** and **repay**.
- **Liquidationcall** is rare, indicating few wallets are liquidated.

---

## 3. Transaction Value Distribution

- The USD value histogram (log scale, colorful) reveals the distribution of transaction sizes.
- **Most transactions are of small value**, with a long tail of larger transactions.
- Outliers or extremely large transactions are easily visible.

---

## 4. Wallet Activity Distribution

- The wallet activity histogram (log scale, colorful) shows how many transactions each wallet has performed.
- **Most wallets are low-activity** (few transactions), while a small number of wallets are highly active.
- This highlights user engagement and possible power users or bots.

---

## 5. Wallet Summary Statistics

- For each wallet, features such as transaction count, total USD value, unique actions, deposit/borrow/repay totals, liquidation count, days active, loan-to-value, and repay ratio are computed.
- These features are used for both EDA and scoring.

---

## 6. Heuristic Credit Scoring Logic

- **Positive behaviors** (increase score):
  - Large deposits
  - High repayment ratio
  - More transactions
  - Diverse actions
  - Longer activity period
- **Negative behaviors** (decrease score):
  - Liquidations
  - High leverage (loan-to-value)
- **Score is bounded between 0 and 1000.**
- Scores are saved as a JSON mapping of wallet addresses to their credit scores.

---

## 7. Insights

- The dataset is generally clean, but some columns are sparse and should be handled with care.
- Most users interact with the protocol in simple ways (deposit/withdraw), while a few are highly active or take on more risk (borrow/repay/liquidate).
- The scoring system rewards responsible and diverse activity, while penalizing risky