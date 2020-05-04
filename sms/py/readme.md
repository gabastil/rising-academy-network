# Validate.py
Glenn Abastillas | May 1, 2020

### How to Use

###### Command

Open a `terminal` or `cmd`, navigate to the script's folder (i.e., `rising-academy-network/sms/py`), and use the following command:

```
python -m validate {USER_ACCESS_KEY} {COUNTRY_CODE}
```

The `USER_ACCESS_KEY` is a 32-digit key that can be obtained by creating an account with [Numverify](http://www.numverify.com). The `COUNTRY_CODE` is a [2-letter code](#country_code) corresponding to the country that the dataset's phone numbers originate from.

A [short list](#country_code) of countries in West Africa can be found below.

###### Example
A `USER_ACCESS_KEY` and `COUNTRY_CODE` for Sierra Leone:

```
python -m validate a14bcd13efg12h11ij10k9l8mn7op698 SL
```

This script reads and writes from a `numbers.csv` document in the `../data` folder. The document must contain the following columns in this order: `number`, `is_valid`, and `checked`.

### Countries and Country Codes of West Africa <a id="country_code"></a>

You can find the [full list of countries](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwiq3ZnexpXpAhUQhHIEHXl3BYgQFjAAegQIAxAB&url=https%3A%2F%2Fwww.iban.com%2Fcountry-codes&usg=AOvVaw1S91ARxH801VYxs3gqhqry) here.

Full Name | 2-Letter Code | 3-Letter Code | Numeric
--- | --- | --- | ---
Benin | BJ | BEN | 204
Burkina Faso | BF | BFA | 854
Cabo Verde | CV | CPV | 132
Gambia (the) | GM | GMB | 270
Ghana | GH | GHA | 288
Guinea-Bissau | GW | GNB | 624
Liberia | LR | LBR | 430
Mali | ML | MLI | 466
Mauritania | MR | MRT | 478
Niger (the) | NE | NER | 562
Nigeria | NG | NGA | 566
Saint Helena, Ascension and Tristan da Cunha | SH | SHN | 654
Senegal | SN | SEN | 686
Sierra Leone | SL | SLE | 694
Togo | TG | TGO | 768