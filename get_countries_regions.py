import requests
import csv

api_url = 'https://goadmin.ifrc.org/api/v2/country/'

region_lookup = {
    0: 'Africa',
    1: 'Americas',
    2: 'Asia Pacific',
    3: 'Europe',
    4: 'MENA'
}

csv_file = 'country_data.csv'

headers = ['iso', 'iso3', 'country_name', 'region_name', 'society_name', 'website']

with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    url = api_url
    
    while url:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            results = data.get('results', [])
            
            for country in results:
                region_name = region_lookup.get(country.get('region'))
                if country.get('iso') and region_name:
                    country_info = {
                        'iso': country.get('iso'),
                        'iso3': country.get('iso3'),
                        'country_name': country.get('name'),
                        'region_name': region_name,
                        'society_name': country.get('society_name'),
                        'website': country.get('website')
                    }
                    writer.writerow(country_info)

            url = data.get('next')
        else:
            print(f"Oops, no results! Error code: {response.status_code}")
            break

print(f"Success! File saved as: {csv_file}")