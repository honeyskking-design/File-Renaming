import os
import pandas as pd
import re

# ---- CONFIG ----
ROOT_DIR = './AnnualReports'         # Change to your reports parent folder
EXCEL_PATH = 'companies.xlsx'        # Your Excel containing codes/symbols
YEAR_SUFFIX = '0331'                 # Suffix for all files (for March 31)
REPORT_PREFIX = 'AR'                 # Prefix (AR) for all renamed files

df = pd.read_excel(EXCEL_PATH)
df['nse_symbol'] = df['nse_symbol'].astype(str).str.strip().str.upper()
df['co_code'] = df['co_code'].astype(str).str.strip()
mapping = df.set_index('nse_symbol').to_dict('index')

for folder in os.listdir(ROOT_DIR):
    folder_path = os.path.join(ROOT_DIR, folder)
    if not os.path.isdir(folder_path):
        continue
    symbol = folder.strip().upper()
    if symbol not in mapping:
        print(f"Symbol '{symbol}' not in Excel mapping; skipping.")
        continue
    code = mapping[symbol]['co_code']

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if not filename.lower().endswith('.pdf'):
            continue
        # Robust year extraction:
        year_match = re.search(r'(\d{4})', filename)
        year = year_match.group(1) if year_match else None
        if year is None:
            print(f"Cannot infer year from file: {filename}; skipping.")
            continue
        new_name = f"{code}_{REPORT_PREFIX}_{year}{YEAR_SUFFIX}.pdf"
        new_path = os.path.join(folder_path, new_name)
        os.rename(file_path, new_path)
        print(f"Renamed {filename} -> {new_name}")

    # Rename the folder itself
    new_folder_name = f"{code} {symbol}"
    new_folder_path = os.path.join(ROOT_DIR, new_folder_name)
    os.rename(folder_path, new_folder_path)
    print(f"Renamed folder {folder} -> {new_folder_name}")
