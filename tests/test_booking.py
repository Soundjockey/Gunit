import requests
from config import *
import pytest


@pytest.mark.webtest 
def test_2_update_booking(test_1_get_token):
    token = test_1_get_token
    print(token)
    r = requests.put(url=url_update, params=params_update)
    print(r.json()) 
    
