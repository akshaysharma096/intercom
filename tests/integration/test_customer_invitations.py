# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>

from typing import Generator
import pytest
from src.constants import (
    DUBLIN_LATITUDE,
    DUBLIN_LONGITUDE, CUSTOMER_DISTANCE
)
import subprocess
from src.db import CustomerDb


class TestCustomerInvitations:

    def test_customer_invitation(self, expected_invited_customers):
        invited_customer_result = subprocess.run(['python3', '-m', 'src'], stdout=subprocess.PIPE)
        assert invited_customer_result.stdout == expected_invited_customers

    def test_customer_db(self):
        customers = CustomerDb.all()
        assert isinstance(customers, Generator)

    def test_invite_customers(self, expected_customers_id_for_100kms):
        invited_customers = CustomerDb.invite_customers(DUBLIN_LONGITUDE, DUBLIN_LATITUDE, CUSTOMER_DISTANCE)
        assert expected_customers_id_for_100kms == sorted(invited_customers.keys())

    @pytest.mark.parametrize(
        'custom_distance, expected_ids',
        [
            (50.0, [4, 5, 6, 11, 12, 15, 31, 39]),
            (10.0, []),
            (20.0, [4]),
            (36.3, [4, 5, 6]),
            (0, []),
            (115.9432, [4, 5, 6, 8, 11, 12, 13, 15, 17, 23, 24, 26, 28, 29, 30, 31, 39])
        ]
    )
    def test_invite_customers_custom_distance(self, custom_distance, expected_ids):
        invited_customers = CustomerDb.invite_customers(DUBLIN_LONGITUDE, DUBLIN_LATITUDE, custom_distance)
        assert expected_ids == sorted(invited_customers.keys())
