import json
import requests
import time
import data
from countryinfo import CountryInfo


def get_sorted_countries():
    url = ("https://restcountries.com/v3.1/all")
    response = requests.get(url)
    if response.status_code == 200:
        countries = response.json()
        sorted_countries = sorted(countries, key=lambda x: x['name']['common'])
        country_names = [country['name']['common'] for country in sorted_countries]
        return country_names
    else:
        print("Не вийшло знайти державу в базі записаних.")

