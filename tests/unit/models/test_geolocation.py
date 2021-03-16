from random import uniform

import pytest

from src.models import GeoLocation


class TestGeoLocation:
    """
        Unit tests to test the GeoLocation model
    """

    @pytest.mark.parametrize(
        'longitude, latitude',
        [
            (56.49281, 16.81308),
            (71.56230, 28.10576),
            (0.0001, 0.0001),
            (-179.99999, -89.99999),
            (179.9999, 89.99999),
        ]
    )
    def test_valid_geolocation(self, longitude, latitude):
        assert isinstance(GeoLocation(longitude, latitude), GeoLocation)

    def test_none_longitude(self):
        random_latitude = uniform(-90.0, 90)
        with pytest.raises(ValueError):
            GeoLocation(None, random_latitude)

    def test_none_latitude(self):
        random_longitude = uniform(-180.0, 180)
        with pytest.raises(ValueError):
            GeoLocation(random_longitude, None)

    def test_none_langitude_latitude(self):
        with pytest.raises(ValueError):
            GeoLocation(None, None)

    @pytest.mark.parametrize(
        'longitude',
        [
            180.00001,
            256.90312,
            -193.9032,
            -180.000001,
            'random_string_1',
            '90.9032'
            '179.99',
            '56.6942'
        ]
    )
    def test_invalid_longitude(self, longitude):
        random_latitude = uniform(-90.0, 90)
        with pytest.raises(ValueError):
            GeoLocation(longitude, random_latitude)

    @pytest.mark.parametrize(
        'latitude',
        [
            90.00001,
            100.2514,
            '45.0012',
            -90.000001,
            'random_string',
            '41.10576'
            '78.90322',
            '56.6942'
        ]
    )
    def test_invalid_latitude(self, latitude):
        random_longitude = uniform(-180.0, 180)
        with pytest.raises(ValueError):
            GeoLocation(random_longitude, latitude)
