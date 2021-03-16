from typing import Generator

from src.constants import DUBLIN_LONGITUDE, DUBLIN_LATITUDE, CUSTOMER_DISTANCE
from src.db import CustomerDb


class TestCustomerDb:
    """
        Unit tests for CustomerDb class.
    """

    def test_customer_db_generator(self):
        customers = CustomerDb.all()
        assert isinstance(customers, Generator)

    def test_invite_customers(self):
        invited_customers = CustomerDb.invite_customers(DUBLIN_LONGITUDE, DUBLIN_LATITUDE, CUSTOMER_DISTANCE)
        assert isinstance(invited_customers, list)
