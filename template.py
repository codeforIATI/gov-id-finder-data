def with_codes(country_code, country_name, example_identifiers):
    return {
      "name": {
        "en": f"{country_name} Chart of Accounts",
        "local": ""
      },
      "url": f"https://gov-id-finder.codeforiati.org/countries/{country_code}/",
      "description": {
        "en": "A government's budget (or 'Chart of Accounts') often refers to government agencies, departments and ministries with stable codes. These can be reliably used in open data publications as identifiers.\n\nThis org-id.guide entry is generated and maintained by Gov Org ID Finder [1] from Development Initiatives. Where available, Gov Org ID Finder extracts and makes Chart of Accounts codes available for the convenience of users. The authoritative source remains the government's budget or Chart of Accounts.\n\n[1] https://gov-id-finder.codeforiati.org/about"
      },
      "coverage": [
        f"{country_code}"
      ],
      "subnationalCoverage": [],
      "structure": [
        "government_agency"
      ],
      "sector": [],
      "code": f"{country_code}-COA",
      "confirmed": True,
      "deprecated": False,
      "listType": "secondary",
      "access": {
        "availableOnline": True,
        "onlineAccessDetails": "Codes can be found in the government budget or Chart of Accounts. Gov Org ID Finder extracts and makes some of these codes available for the convenience of users. The authoritative source remains the government's budget or Chart of Accounts.",
        "publicDatabase": f"https://gov-id-finder.codeforiati.org/countries/{country_code}/",
        "guidanceOnLocatingIds": "The codes from the Organisation or Administrative classification should be used. ",
        "exampleIdentifiers": f"{example_identifiers}",
        "languages": [
          "en"
        ]
      },
      "data": {
        "availability": [
          "json", "csv"
        ],
        "dataAccessDetails": f"A download of the data is available from https://gov-id-finder.codeforiati.org/countries/{country_code}/",
        "features": [],
        "licenseStatus": "no_license",
        "licenseDetails": ""
      },
      "meta": {
        "source": "Desk research",
        "lastUpdated": "2022-03-23"
      },
      "links": {
        "opencorporates": "",
        "wikipedia": ""
      },
      "formerPrefixes": []
    }

def without_codes(country_code, country_name):
    return {
      "name": {
        "en": f"{country_name} Chart of Accounts",
        "local": ""
      },
      "url": f"https://gov-id-finder.codeforiati.org/countries/{country_code}/",
      "description": {
        "en": "A government's budget (or 'Chart of Accounts') often refers to government agencies, departments and ministries with stable codes. These can be reliably used in open data publications as identifiers.\n\nThis org-id.guide entry is generated and maintained by Gov Org ID Finder [1] from Development Initiatives. Where available, Gov Org ID Finder extracts and makes Chart of Accounts codes available for the convenience of users. The authoritative source remains the government's budget or Chart of Accounts.\n\n[1] https://gov-id-finder.codeforiati.org/about"
      },
      "coverage": [
        f"{country_code}"
      ],
      "subnationalCoverage": [],
      "structure": [
        "government_agency"
      ],
      "sector": [],
      "code": f"{country_code}-COA",
      "confirmed": True,
      "deprecated": False,
      "listType": "secondary",
      "access": {
        "availableOnline": False,
        "onlineAccessDetails": f"Codes can be found in the government budget or Chart of Accounts. Gov Org ID Finder extracts and makes some of these codes available for the convenience of users. However, no codes have yet been extracted for {country_name}.",
        "publicDatabase": f"https://gov-id-finder.codeforiati.org/countries/{country_code}/",
        "guidanceOnLocatingIds": "",
        "exampleIdentifiers": "",
        "languages": []
      },
      "data": {
        "availability": [],
        "dataAccessDetails": "Look at the government budget or Chart of Accounts. If you find identifiers, you can also submit them for inclusion to Gov Org ID Finder: https://gov-id-finder.codeforiati.org/about",
        "features": [],
        "licenseStatus": "no_license",
        "licenseDetails": ""
      },
      "meta": {
        "source": "Desk research",
        "lastUpdated": "2022-03-23"
      },
      "links": {
        "opencorporates": "",
        "wikipedia": ""
      },
      "formerPrefixes": []
    }