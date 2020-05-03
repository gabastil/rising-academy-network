#!/usr/bin/env python
# author: Glenn Abastillas
# created: May 1, 2020
# description: A simple script to validate phone numbers

from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from sys import argv
import json
import csv

url = "http://apilayer.net/api/validate?"


def validate(access_key, number, country_code):
    ''' Return whether or not a phone number is valid

        Parameters
        ----------
            access_key (str): 32-digit user access key for API
            number (str, int): Phone number to check
            country_code (str): 2-letter country code for the phone number

        Returns
        -------
            True or false if the API provides a proper response.
            None if the API does not provide a proper response.
    '''
    try:
        query = urlencode({'access_key': access_key,
                           'number': number,
                           'country_code': country_code})

        result = urlopen(url + query)

        if result.status == 200:
            response = json.loads(result.read())

            if 'valid' in response:
                return response['valid']
            print(response['error']['info'])

    except (HTTPError, URLError) as e:
        print(e.reason)


def read_csv(path):
    numbers = []
    with open(path, newline='') as numbers_csv:
        for line in csv.reader(numbers_csv):
            numbers.append(line)
    return numbers


def to_csv(data, path):
    with open(path, 'w', newline='') as numbers_csv:
        writer = csv.writer(numers_csv)
        for row in data:
            writer.writerow(row)


def checked(check):
    ''' Indicate whether or not a phone number has already been checked '''
    return check.lower().startswith('t')


if __name__ == "__main__":
    user_access_key, country_code = argv[1:3]
    data_path = "../data/numbers.csv"
    print(f'\nPhone Number Verification for {country_code}\n{"":-<80}')

    # Ensure user access key is of valid type and length
    assert isinstance(user_access_key, str) and len(user_access_key) < 33

    numbers = read_csv(data_path)

    # Assumes indices : 'number' at 0, 'is_valid' at 1, 'checked' at 2
    for row in numbers[1:]:

        if not checked(row[2]):
            result = validate(user_access_key, int(row[0]), country_code)

            if result is None:
                break

            row[1] = 'True' if result else 'False'
            row[2] = 'True'

    to_csv(numbers, data_path)
    print(f'{"":-<80}\nVerification Process Completed')
