import pandas as pd
import openpyxl
import os

def run_xlsx():
	files = [fn for fn in os.listdir('data/xlsx') if (fn.endswith('.xlsx') and not fn.startswith('~'))]
	for file in files:
		df = pd.read_excel(f'data/xlsx/{file}', dtype=str, keep_default_na=False)
		country_code = file.split('.')[0]
		df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
		df.to_csv(f'data/{country_code}.csv', index=False)

run_xlsx()
