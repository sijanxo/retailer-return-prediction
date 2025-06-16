# Retailer Ticket Return Prediction using Machine Learning

This project analyzes scratch-off ticket return data from lottery retailers and uses machine learning to predict whether a retailer is likely to have a **high volume of returns** in a given month.

## 📊 Dataset

The dataset includes scratch-off return records from multiple fiscal years (2023–2025) with columns like:

- `RetailerID`, `ProductID`
- `ReturnDate`
- `PricePoint`, `TotalPrice`
- Product and ticket details

## 🧠 Goal

Predict if a retailer will have **above-average (high)** ticket returns in a given month using:

- Retailer ID
- Product ID
- Return month
- Price point
- Number of products returned

## 🛠️ Methods

- Label encoding for categorical variables
- Extracted month from return dates
- Grouped by retailer and month for aggregation
- Created binary target label (`HighReturn`)
- Trained a **Random Forest Classifier**
- Evaluated using accuracy, precision, recall, and F1-score

## ✅ Results

- Achieved **~83% accuracy** across all tested fiscal years
- Balanced precision/recall for predicting high-return cases

## 📁 Files

- `ticket_return_model.py` – main Python script
- `sample_data.csv` – dummy dataset for testing (no real company data)
- `generate_dummy_data.py` – optional script to generate synthetic data

## ▶️ How to Run

1. Load your data (e.g., `f2023`, `f2024`) into a Pandas DataFrame
2. Call the `process_and_train()` function with your DataFrame:

```python
from ticket_return_model import process_and_train

process_and_train(f2023)
