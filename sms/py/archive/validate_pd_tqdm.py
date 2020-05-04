#!/usr/bin/env python
# author: Glenn Abastillas
# created: May 1, 2020
# description: A simple script to validate phone numbers

from sys import argv
from tqdm import tqdm
import pandas as pd
import requests
import json

url = "http://apilayer.net/api/validate?access_key={}&number={}&country_code={}"


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
    request = url.format(access_key, number, country_code)
    result = requests.get(request)

    if result.status_code == 200:
        response = json.loads(result.content)

        if 'valid' in response:
            return response['valid']


if __name__ == "__main__":
    user_access_key, country_code = argv[1:3]
    data_path = "../data/numbers.csv"

    # Ensure user access key is of valid type and length
    assert isinstance(user_access_key, str) and len(user_access_key) < 33

    header = 'Phone Number Verification\nUser Access Key:{}\nCountry Code:{}\n'
    print(header.format(user_access_key, country_code))

    data = pd.read_csv(data_path)

    total = (data.checked == False).sum()
    count = 0

    for i, row in tqdm(data.iterrows(), total=total):

        if row.checked == False:
            result = validate(user_access_key, int(row.number), country_code)

            if result is None:
                break

            elif result:
                count += 1
                data.loc[i, 'is_valid'] = True

            else:
                data.loc[i, 'is_valid'] = False

            data.loc[i, 'checked'] = True

    data.to_csv(data_path, index=False)
    percent = count / total * 100
    print(f'{percent:.1%} of {total} are valid.')
