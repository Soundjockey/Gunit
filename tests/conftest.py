import pytest
import requests
from config import *


@pytest.fixture()
def test_1_get_token():
    token = requests.post(url=url_token, json=params)
    return token.json()
