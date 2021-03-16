import pytest

from src.models import Customer, GeoLocation


class TestCustomer:

    """
        Unit tests for the Customer model.
    """

    @pytest.mark.parametrize(
        'user_id, name, geo_location',
        [
            (901, 'Ronaldo', GeoLocation(-9.742744, 51.999447)),
            (178, 'Roger Waters', GeoLocation(-7.11167, 53.74452))
        ]
    )
    def test_valid_customer(self, user_id, name, geo_location):
        Customer(user_id, name, geo_location)
