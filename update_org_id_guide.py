import requests
import csv
import template
import os
import json

COUNTRY_URL = "https://codelists.codeforiati.org/api/json/en/Country.json"

# AF-COA has already been created on org-id.guide, so we ignore it
EXCLUDED_COUNTRIES = 'AF'

def run():
    countries = requests.get(COUNTRY_URL).json().get('data')
    with open('docs/source/metadata.csv', 'r') as metadata_f:
        csvreader = csv.DictReader(metadata_f)
        countries_with_codes = dict([(row['Country_code'], row) for row in csvreader])

    for country in countries:
        if country['code'] in EXCLUDED_COUNTRIES: continue
        if country['status'] == 'withdrawn': continue
        if country['code'] in countries_with_codes:
            make_country_with_codes(country)
        else:
            make_country_without_codes(country)


def write_data(lowercase_country_code, data):
    path_to_codelist_dir = os.path.join(
        'orgid_repo', 'lists', lowercase_country_code)
    os.makedirs(path_to_codelist_dir, exist_ok=True)
    with open(os.path.join(path_to_codelist_dir, '{}-coa.json'.format(lowercase_country_code)), 'w') as out_jsonf:
        json.dump(data, out_jsonf, indent=2)


def make_country_with_codes(country):
    country_code = country['code']
    country_name = country['name']
    lowercase_country_code = country_code.lower()
    with open(f'docs/source/{country_code}.csv', 'r') as country_codes_f:
        csvreader = csv.DictReader(country_codes_f)
        coa_codes = [list(row.values())[0] for row in csvreader]
        example_identifiers = ", ".join(coa_codes[0:2])
    data = template.with_codes(country_code, country_name, example_identifiers)
    print(f"Making country {country_code}")
    write_data(lowercase_country_code, data)


def make_country_without_codes(country):
    country_code = country['code']
    country_name = country['name']
    lowercase_country_code = country_code.lower()
    data = template.without_codes(country_code, country_name)
    print(f"Making no codes for country {country_code}")
    write_data(lowercase_country_code, data)


run()
