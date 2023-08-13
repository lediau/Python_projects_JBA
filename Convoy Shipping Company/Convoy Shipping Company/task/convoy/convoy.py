# Write your code here
import pandas as pd

excel_file = input('Input file name\n')
my_df = pd.read_excel(excel_file, sheet_name='Vehicles', dtype=str)
csv_file = excel_file.removesuffix('.xlsx') + '.csv'
my_df.to_csv(csv_file, index=None)
n = my_df.shape[0]
print(f'{n} line{"s were" if n > 1 else " was"} imported to {csv_file}')
