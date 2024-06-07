#!/usr/bin/env python3

"""
This also requires having XlsxWriter installed in the env though it doesn't have to be imported. 
Use `pip install XlsxWriter`
"""

import pandas as pd

file_path = 'country_data.xlsx'
workbook = pd.ExcelFile(file_path)

country_data = workbook.parse('country_data')
cluster_data = workbook.parse('cluster_data')

def find_cluster_id(country_name):
	for index, row in cluster_data.iterrows():
		if country_name in row['countries']:
			return row['cluster_id']
	return None

country_data['cluster_id'] = country_data['country_name'].apply(find_cluster_id)

output_file_path = 'country_region_cluster.xlsx' 
with pd.ExcelWriter(output_file_path, engine='xlsxwriter') as writer:
	country_data.to_excel(writer, sheet_name='country_data', index=False)
	cluster_data.to_excel(writer, sheet_name='cluster_data', index=False) 
	
print(f"Success! Saved to: {output_file_path}")