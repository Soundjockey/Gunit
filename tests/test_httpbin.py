import requests
from Config_test import *
import pytest


@pytest.fixture()
def test_get_datetime():
    current_time = datetime.datetime.now()
    return current_time
    #r = requests.get(url=url_test, params=params_test)
    #print(r.json())