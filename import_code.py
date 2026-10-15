import os
from urllib.parse import quote_plus
import pandas as pd
from sqlalchemy import create_engine, text

# 1. Exact CSV path relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "accepted_2007_to_2018Q4.csv")

# 2. Columns to extract
cols_to_keep = [
    'id', 'loan_amnt', 'term', 'int_rate', 'grade', 'sub_grade',
    'emp_length', 'home_ownership', 'annual_inc', 'issue_d',
    'loan_status', 'purpose', 'addr_state', 'dti', 'delinq_2yrs',
    'fico_range_low', 'fico_range_high', 'revol_util'
]

# Rename loan_amnt to loan_amount to match SQL table schema
rename_map = {
    'loan_amnt': 'loan_amount'
}

# 3. Database connection
DB_USER = "postgres"
DB_PASS = quote_plus("Vartiksrivastav73@")
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "bfsi_credit_risk"

connection_url = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(connection_url)

# Ensure string columns are TEXT to prevent StringDataRightTruncation errors
text_cols = ['loan_status', 'purpose', 'addr_state', 'emp_length', 'home_ownership', 'id', 'issue_d', 'term', 'grade', 'sub_grade']
with engine.begin() as conn:
    for col in text_cols:
        conn.execute(text(f"ALTER TABLE raw_loan_data ALTER COLUMN {col} TYPE TEXT;"))
    result = conn.execute(text("SELECT count(*) FROM raw_loan_data;"))
    existing_rows = result.scalar() or 0

print(f"Connecting to database '{DB_NAME}'...")
if existing_rows > 0:
    print(f"Found {existing_rows:,} existing rows in 'raw_loan_data'. Resuming from row {existing_rows + 1:,}...")
    skiprows = range(1, existing_rows + 1)
    total_rows = existing_rows
    start_batch = existing_rows // 50000
else:
    print("Starting fresh import into PostgreSQL...")
    skiprows = None
    total_rows = 0
    start_batch = 0

chunksize = 50000

csv_reader = pd.read_csv(
    csv_path,
    usecols=cols_to_keep,
    chunksize=chunksize,
    skiprows=skiprows,
    low_memory=False
)

for i, chunk in enumerate(csv_reader):
    batch_num = start_batch + i + 1
    chunk = chunk.rename(columns=rename_map)
    chunk.to_sql('raw_loan_data', engine, if_exists='append', index=False)
    total_rows += len(chunk)
    print(f"Batch {batch_num} completed -> Total rows loaded: {total_rows:,}")

print(f"\nAll done! Successfully loaded {total_rows:,} records into 'raw_loan_data'.")
