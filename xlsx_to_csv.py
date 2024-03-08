import pandas as pd
import openpyxl
import os

def run_xlsx():
	files = [fn for fn in os.listdir('data/xlsx') if (fn.endswith('.xlsx') and not fn.startswith('~'))]
	for file in files:
		df = pd.read_excel(f'data/xlsx/{file}')
		country_code = file.split('.')[0]
		df.to_csv(f'data/{country_code}.csv', index=False)

run_xlsx()
