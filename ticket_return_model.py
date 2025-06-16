import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from datetime import datetime

def process_and_train(df, threshold=None):
    """
    Processes the ticket return data, trains a Random Forest classifier to predict high return months,
    and prints evaluation metrics.
    """

    df = df.copy()

    # Encode categorical features
    le_r = LabelEncoder()
    le_p = LabelEncoder()
    df['RetailerID_Encoded'] = le_r.fit_transform(df['RetailerID'])
    df['ProductID_Encoded'] = le_p.fit_transform(df['ProductID'])

    # Extract month from ReturnDate
    def get_month(date_string):
        try:
            return datetime.strptime(date_string, "%m/%d/%Y").month
        except:
            return None
    df['ReturnMonth'] = df['ReturnDate'].apply(get_month)
    df = df.dropna(subset=['ReturnMonth'])

    # Aggregate by Retailer and Month
    grouped = df.groupby(['RetailerID_Encoded', 'ReturnMonth']).agg({
        'TotalPrice': 'sum',
        'PricePoint': 'mean',
        'ProductID_Encoded': 'count'
    }).reset_index()

    # Define threshold for HighReturn label
    if threshold is None:
        threshold = grouped['TotalPrice'].mean()
    grouped['HighReturn'] = (grouped['TotalPrice'] > threshold).astype(int)

    # Prepare features and labels
    X = grouped[['RetailerID_Encoded', 'ReturnMonth', 'PricePoint', 'ProductID_Encoded']]
    y = grouped['HighReturn']

    # Split data and train model
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Evaluation
    print(f"Threshold for HighReturn: {threshold:.2f}")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    # Example: you should load f2023, f2024 beforehand
    process_and_train(f2023)
    process_and_train(f2024)
