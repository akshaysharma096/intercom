import pytest


@pytest.fixture(scope='module')
def sample_customers():
    return "{'latitude': '34.83445', 'user_id': 901, 'name': 'Robert Plant', 'longitude': '-36.16288'}\n" \
           "{'latitude': '52.986375', 'user_id': 12, 'name': 'Jimmy Page', 'longitude': '-6.043701'}\n" \
           "{'latitude': '-50.99210', 'user_id': 231, 'name': 'Jimi Hendrix', 'longitude': '105.02913'}\n" \
           "{'latitude': '53.2451022', 'user_id': 4, 'name': 'David Gilmour', 'longitude': '-6.238335'}\n" \
           "{'latitude': '53.0033946', 'user_id': 2392, 'name': 'David Gilmour', 'longitude': '-6.3877505'}"
