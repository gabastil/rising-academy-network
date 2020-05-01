#!/usr/bin/env python
# author: Glenn Abastillas
# created: May 1, 2020
# description: A simple script to verify phone numbers

from sys import argv
import json
from tqdm import tqdm
import pandas as pd
import requests

endpoint = "http://apilayer.net/api/validate?"

def validate_number(key, number, country_code):
    ''' Return a tuple with information about a phone number '''

    access_key = f"access_key={key}"
    number_ = f"&number={number}"
    country_code = f"&country_code={country_code}"

    result = requests.get(api)

    if result.status_code == 200:
        response = json.loads(result.content)
        return response['valid']


if __name__ == "__main__":
    user_access_key = argv[1]
    country_code = argv[2]

    assert isinstance(user_access_key, str) and len(user_access_key) > 5

    print('\nRISING ACADEMY NETWORK Phone Number Verification')
    print(f'USER ACCESS KEY: {user_access_key}')
    print(f'COUNTRY CODE: {country_code}')
    print('-' * 80)

    data = pd.read_csv("../data/numbers.csv")

    is_valid, is_valid_count = [], 0

    for i, row in tqdm(data.iterrows()):
        valid_ = validate_number(user_access_key, row.number, country_code)

        is_valid.append(valid_)

        if valid_:
            is_valid_count_ += 1

    data = data.assign(is_valid=is_valid)
    data.to_csv("../data/numbers_validated.csv", index=False)
    print(f'{is_valid_count / data.shape[0]} valid numbers founds.')
