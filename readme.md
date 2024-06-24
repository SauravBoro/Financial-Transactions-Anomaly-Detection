# Financial Transactions Anomaly Detection

## Overview

This project involves developing a system to identify and report anomalies in a dataset of financial transactions. The script processes a large dataset, calculates statistical thresholds, and flags transactions that deviate significantly from typical patterns.

## Features

- Data preprocessing to clean and standardize the dataset.
- Calculation of statistical metrics like mean, median, and standard deviation.
- Anomaly detection using Z-score and Interquartile Range (IQR) methods.
- Detailed report generation listing detected anomalies with reasons.

## Usage

1. Place your dataset in the project directory. The dataset should be a CSV file with the following columns:
    - `transaction_id`
    - `date`
    - `category`
    - `amount`

2. Update the `file_path` variable in the script to the path of your CSV file:

    ```python
    file_path = '/path/to/your/transactions.csv'
    ```

3. Run the script:

    ```sh
    python3 Transactions-Anomaly-Detection.py
    ```

4. The script will generate a report of detected anomalies and save it as `anomalies_report.csv` in the project directory.

## Detailed Steps

### 1. Data Preprocessing

- **Loading Data:** The script loads the dataset from a CSV file.
- **Cleaning Data:** The script handles missing values and converts date strings to datetime objects for proper analysis.

### 2. Statistical Analysis

- **Grouping by Category:** Transactions are grouped by their category to calculate category-specific statistics.
- **Calculating Metrics:** The script computes the mean, median, and standard deviation for transaction amounts in each category.

### 3. Anomaly Detection

- **Z-score Calculation:** The script calculates the Z-score for each transaction amount. Transactions with a Z-score greater than 3 or less than -3 are flagged as anomalies.
- **IQR Calculation:** The script calculates the Interquartile Range (IQR) and flags transactions that fall outside the bounds of Q1 - 1.5*IQR and Q3 + 1.5*IQR as anomalies.
- **Flagging Anomalies:** Each flagged transaction is recorded with a reason for why it was flagged.

### 4. Report Generation

- **Creating the Report:** The script generates a detailed report of all detected anomalies.
- **Saving the Report:** The report is saved as `anomalies_report.csv` in the project directory.

## Example

Here is a sample representation of the transaction dataset:

```csv
transaction_id,date,category,amount
TRX001,2024-06-01,Food,25.00
TRX002,2024-06-01,Utilities,150.00
TRX003,2024-06-01,Entertainment,200.00
TRX004,2024-06-02,Food,3000.00  # Anomalous high amount
TRX005,2024-06-02,Transport,45.00
TRX006,2024-06-03,Utilities,135.00
TRX007,2024-06-03,Food,20.00
