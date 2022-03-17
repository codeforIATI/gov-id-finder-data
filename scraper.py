import csv
import json
import sys
from pathlib import Path
from collections import defaultdict
from itertools import zip_longest
from urllib.parse import quote_plus
from os import environ, listdir, makedirs
from datetime import datetime

import orgidfinder


def zip_discard_compr(*iterables, sentinel=None):
    return [[entry for entry in iterable if entry is not sentinel]
            for iterable in zip_longest(*iterables, fillvalue=sentinel)]

output_dir = Path('docs')
scrape_started_at = datetime.now().isoformat()

guide = orgidfinder.setup_guide()

data = []

countries = {}

makedirs(f'{output_dir}/source', exist_ok=True)


def copy_csvfile(filename, newFilename, encoding_from, encoding_to='UTF-8'):
    with open(filename, 'r', encoding=encoding_from) as fr:
        with open(newFilename, 'w', encoding=encoding_to) as fw:
            for line in fr:
                fw.write(line[:-1]+'\r\n')


with open('data/metadata.csv', 'r', encoding='utf-8-sig') as metadata_f:
    metadata_csv = csv.DictReader(metadata_f)
    for row in metadata_csv:
        countries[row['Country_code']] = row

copy_csvfile('data/metadata.csv', f'{output_dir}/source/metadata.csv', 'utf-8-sig')

filenames = sorted([filename for filename in listdir('data') if filename.endswith('.csv') and filename != 'metadata.csv'])
for filename in filenames:
    copy_csvfile(f'data/{filename}', f'{output_dir}/source/{filename}', 'ISO-8859-1')
    org_infos = orgidfinder.parse_csv_file(countries, f'data/{filename}')
    for org_info in org_infos:
        org_info['org_type'] = guide._org_types.get(org_info['org_type_code'])
        id_ = quote_plus(org_info['org_id'])
        with open(Path(f'{output_dir}/data/{id_}.json'), 'w') as f:
            json.dump(org_info, f)
        data.append(org_info)

with open(Path(f'docs/downloads/org-ids.json'), 'w') as f:
    json.dump(data, f)

fieldnames = ['org_id', 'name', 'org_type', 'org_type_code', 'source_dataset', 'source_url']
with open(Path(f'docs/downloads/org-ids.csv'), 'w') as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for d in data:
        w.writerow({f: d.get(f, '') if f != 'name' else d['name'][d['lang']] for f in fieldnames})

counter = defaultdict(set)
minlen = 3
for d in data:
    default_lang = d['lang']
    default_name = d['name'].get(default_lang)

    text = d['org_id'].lower()
    for subtext in set([text[i: j] for i in range(len(text)) for j in range(i + 1, len(text) + 1) if len(text[i:j]) == minlen]):
        counter[subtext].add((default_name, d['org_id']))

    for lang, name in d['name'].items():
        text = name.lower()
        if lang != default_lang:
            name += ' ({})'.format(d['name'][default_lang])
        for subtext in set([text[i: j] for i in range(len(text)) for j in range(i + 1, len(text) + 1) if len(text[i:j]) == minlen]):
            counter[subtext].add((name, d['org_id']))

for k, v in sorted(counter.items()):
    sorted_v = sorted(v, key=lambda x: x[0])
    quoted_k = quote_plus(k)
    with open(Path(f'{output_dir}/data/lookup/{quoted_k}.json'), 'w') as f:
        json.dump(sorted_v, f)

scrape_finished_at = datetime.now().isoformat()
with(open(Path(f'{output_dir}/data/status.json'), 'w')) as f:
    json.dump({
        'started_at': scrape_started_at,
        'finished_at': scrape_finished_at,
    }, f)
