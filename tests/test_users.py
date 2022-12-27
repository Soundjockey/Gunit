import requests

from Config_test import *


def registration_on_the_site():
    token = requests.post(url=url, params=params) 
    print(token.json())