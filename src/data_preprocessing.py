import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(path="data/wine.csv"):
    return pd.read_csv(path)

def clean_data(df):
    # Fill missing values
    df = df.fillna(df.median(numeric_only=True))
    # Remove outliers using IQR
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    df_cleaned = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)].copy()
    return df_cleaned

def scale_features(df):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df)
    return X_scaled