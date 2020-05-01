#!/usr/bin/env python
# author: Glenn Abastillas
# created: May 1, 2020
# description: A simple script to validate phone numbers

from sys import argv
from tqdm import tqdm
import pandas as pd
import requests
import json

url = ("http://apilayer.net/api/validate?"
       "access_key={}&number={}&country_code={}")


def validate(access_key, number, country_code):
    ''' Return the validity status of a phone number

        Parameters
        ----------
            access_key (str) : 32-digit user access key for API
            number (str, int) : Phone number to check
            country_code (str) : 2 character country code for the phone number

        Returns
        -------
            True or false if the API provides a proper response.
            None if the API does not provide a proper response.
    '''

    api = url.format(access_key, int(number), country_code)
    result = requests.get(api)

    if result.status_code == 200:
        response = json.loads(result.content)

        if 'valid' not in response:
            return None

        return response['valid']


if __name__ == "__main__":
    user_access_key, country_code = argv[1:3]

    # Ensure user access key is of valid type and length
    assert isinstance(user_access_key, str) and len(user_access_key) < 33

    print(f'\nPhone Number Verification'
          f'\nUser Access Key: {user_access_key}'
          f'\nCountry Code: {country_code}'
          f'\n{"":->80}')

    data = pd.read_csv("../data/numbers.csv")
    total = (data.checked == False).sum()

    valid_count = 0

    for i, row in tqdm(data.iterrows(), total=total):

        if row.checked == False:
            valid_ = validate(user_access_key, row.number, country_code)

            if valid_ is None:
                break

            elif valid_:
                valid_count += 1
                data.loc[i, 'is_valid'] = True

            data.loc[i, 'checked'] = True

    data.to_csv("../data/numbers.csv", index=False)
    print(f'{valid_count / total * 100:.1%} of {total} are valid.')
