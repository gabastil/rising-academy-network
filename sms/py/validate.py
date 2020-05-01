#!/usr/bin/env python
# author: Glenn Abastillas
# created: May 1, 2020
# description: A simple script to validate phone numbers

from sys import argv
import json
from tqdm import tqdm
import pandas as pd
import requests

endpoint = "http://apilayer.net/api/validate?" +\
           "access_key={}&number={}&country_code={}"


def validate_number(access_key, number, country_code):
    ''' Return a tuple with information about a phone number '''

    api = endpoint.format(access_key, int(number), country_code)
    result = requests.get(api)

    if result.status_code == 200:
        response = json.loads(result.content)
        if 'valid' not in response:
            return None
        return response['valid']


if __name__ == "__main__":
    user_access_key = argv[1]
    country_code = argv[2]

    assert isinstance(user_access_key, str) and len(user_access_key) > 5

    print('\nPHONE NUMBER VERIFICATION')
    print(f'USER ACCESS KEY: {user_access_key}')
    print(f'COUNTRY CODE: {country_code}')
    print('-' * 80)

    data = pd.read_csv("../data/numbers.csv")
    total = (data.checked == False).sum()

    is_valid, valid_count = [], 0

    for i, row in tqdm(data.iterrows(), total=total):

        if row.checked is False:
            valid_ = validate_number(user_access_key, row.number, country_code)

            if valid_:
                valid_count += 1
                data.loc[i, 'is_valid'] = True

            if valid_ is None:
                break

            data.loc[i, 'checked'] = True

    data.to_csv("../data/numbers_validated.csv", index=False)
    print(f'{valid_count / total * 100:.1%} of {total} are valid.')
