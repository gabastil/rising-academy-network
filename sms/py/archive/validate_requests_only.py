#!/usr/bin/env python
# author: Glenn Abastillas
# created: May 1, 2020
# description: A simple script to validate phone numbers

from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import requests
import json
import csv

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


def read_csv(path):
    numbers = []
    with open(path) as numbers_data:
        for line in csv.reader(numbers_data):
            numbers.append(line)
    return numbers


def to_csv(data, path):
    data = [','.join(line) for line in data]
    with open(path, 'w') as numbers_data:
        data = '\n'.join(data)
        numbers_data.write(data)


def checked(check):
    ''' Determine if the number has already been checked '''
    return check.lower().startswith('t')


if __name__ == "__main__":
    user_access_key, country_code = argv[1:3]
    data_path = "../data/numbers.csv"
    print(f'Phone Number Verification with Key {user_access_key}\n{"":-<80}')

    # Ensure user access key is of valid type and length
    assert isinstance(user_access_key, str) and len(user_access_key) < 33

    header, *numbers = read_csv(data_path)

    # Assumes indices : 'number' at 0, 'is_valid' at 1, 'checked' at 2
    for row in numbers:

        if not checked(row[2]):
            result = validate(user_access_key, int(row[0]), country_code)

            if result is None:
                print('Call limit likely reached.')
                break

            row[1] = 'False'

            if result:
                row[1] = 'True'

            row[2] = 'True'

    to_csv([header] + numbers, data_path)
    print(f'Verification loop completed.')
