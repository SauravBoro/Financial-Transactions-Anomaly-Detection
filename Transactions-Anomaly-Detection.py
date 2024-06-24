import pandas as pd
import numpy as np

file_path = 'transactions.csv'
df = pd.read_csv(file_path)
df['date'] = pd.to_datetime(df['date'])
df.dropna(inplace=True)

stats = df.groupby('category')['amount'].agg(['mean', 'std', 'median']).reset_index()

def detect_anomalies(row, stats):
    category_stats = stats[stats['category'] == row['category']]
    if category_stats.empty:
        return False, ''
    
    mean = category_stats['mean'].values[0]
    std = category_stats['std'].values[0]
    z_score = (row['amount'] - mean) / std
    
    if abs(z_score) > 1.5:
        return True, f"Z-score {z_score:.2f} > 1.5"
    
    q1 = df[df['category'] == row['category']]['amount'].quantile(0.25)
    q3 = df[df['category'] == row['category']]['amount'].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 0.5 * iqr
    upper_bound = q3 + 0.5 * iqr
    
    if row['amount'] < lower_bound or row['amount'] > upper_bound:
        return True, f"Outside IQR bounds ({lower_bound}, {upper_bound})"
    
    return False, ''

# Detect anomalies
anomalies = []
for idx, row in df.iterrows():
    is_anomaly, reason = detect_anomalies(row, stats)
    if is_anomaly:
        anomalies.append({
            'transaction_id': row['transaction_id'],
            'date': row['date'],
            'category': row['category'],
            'amount': row['amount'],
            'reason_for_anomaly': reason
        })

anomalies_df = pd.DataFrame(anomalies)

report_file_path = 'anomalies_report.csv'
anomalies_df.to_csv(report_file_path, index=False)
