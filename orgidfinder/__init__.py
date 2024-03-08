from . import orgidguide
import csv


ns = 'http://www.w3.org/XML/1998/namespace'


def get_text(el, path, default_lang):
    text = {}
    narratives = el.xpath('{}/narrative'.format(path))
    if narratives != []:
        for narrative in narratives:
            lang = narrative.attrib.get('{{{}}}lang'.format(ns), default_lang)
            # this is a silly hack to prefer the first occurrence
            # of a string for a given language, rather than the last
            if lang not in text:
                text[lang] = narrative.text
    else:
        # v1.0x, I guess
        text[default_lang] = el.find(path).text
    return text


def parse_org(organisation):
    org_id = organisation.id
    reporting_org_id = organisation.etree.find('reporting-org').get('ref')
    if not reporting_org_id or org_id != reporting_org_id:
        return None

    default_lang = organisation.etree.attrib.get('{{{}}}lang'.format(ns), 'en')
    reporting_name = get_text(organisation.etree, 'reporting-org', default_lang)
    org_type_code = organisation.etree.find('reporting-org').get('type')

    try:
        org_name = get_text(organisation.etree, 'name', default_lang)
    except AttributeError:
        org_name = {}
    if not org_id or not org_name:
        # couldn't find an org name, so just use reporting-org
        if reporting_name:
            org_name = reporting_name
        else:
            return None

    if not org_name.get(default_lang):
        if len(org_name) > 1:
            print('Unclear which lang should be default')
        default_lang = list(org_name.keys())[0]

    return {
        'lang': default_lang,
        'name': org_name,
        'org_id': org_id,
        'org_type_code': org_type_code,
    }


def parse_org_file(dataset):
    all_data = []
    for organisation in dataset.organisations:
        data = parse_org(organisation)
        if not data:
            continue
        data['source_url'] = dataset.metadata['resources'][0]['url']
        data['source_dataset'] = dataset.name
        all_data.append(data)
    return all_data


def parse_csv_org(countries, country_code, organisation):
    keys = list(organisation.keys())
    values = list(organisation.values())
    lang = keys[1].split("_")[1].lower()
    country_name = countries[country_code]['Country_name'].strip()
    org_name = {lang: '{} ({})'.format(values[1].strip(), country_name.strip())}
    org_name_simple = {lang: '{}'.format(values[1].strip())}
    org_id = "{}-COA-{}".format(country_code, values[0].strip())
    org_type_code = "10"
    return {
        'lang': lang,
        'name': org_name,
        'name_simple': org_name_simple,
        'country_code': country_code,
        'country_name': country_name,
        'org_id': org_id,
        'org_type_code': "10",
    }


def parse_csv_file(countries, filename):
    all_data = []
    with open(filename, 'r', encoding='ISO-8859-1') as _file:
        country_code, _ = filename.split("/")[1].split(".")
        rows = csv.DictReader(_file)
        for organisation in rows:
            data = parse_csv_org(countries, country_code, organisation)
            if not data:
                continue
            data['source_url'] = countries[country_code]['Source']
            data['source_dataset'] = '{} Budget'.format(countries[country_code]['Year'])
            all_data.append(data)
    return all_data


def setup_guide():
    '''
    Factory for OrgIDGuide
    '''
    return orgidguide.OrgIDGuide()
