import random
import string

import pytest

from src.models import GeoLocation


@pytest.fixture(scope='module')
def random_name():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10))


@pytest.fixture(scope='module')
def random_longitude():
    return random.uniform(-180.0, 180.0)


@pytest.fixture(scope='module')
def random_latitude():
    return random.uniform(-90.0, 90.0)


@pytest.fixture(scope='module')
def random_distance():
    return random.uniform(50, 1000)


@pytest.fixture(scope='module')
def random_geolocations():
    longitude_1 = random.uniform(-180.0, 180.0)
    latitude_1 = random.uniform(-90.0, 90.0)
    longitude_2 = random.uniform(-180.0, 180.0)
    latitude_2 = random.uniform(-90.0, 90.0)
    return GeoLocation(longitude_1, latitude_1), GeoLocation(longitude_2, latitude_2)


@pytest.fixture(scope='module')
def random_geolocation():
    longitude_1 = random.uniform(-180.0, 180.0)
    latitude_1 = random.uniform(-90.0, 90.0)
    return GeoLocation(longitude_1, latitude_1)
