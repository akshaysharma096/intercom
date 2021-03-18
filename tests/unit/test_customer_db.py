# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>

from typing import Generator

import pytest

from src.db import CustomerDb


class TestCustomerDb:
    """
        Unit tests for CustomerDb class.
    """

    def test_customer_db_generator(self):
        customers = CustomerDb.all()
        assert isinstance(customers, Generator)

    def test_invite_customers(self, random_longitude, random_latitude, random_distance):
        result_set = CustomerDb.invite_customers(random_longitude, random_latitude, random_distance)
        assert isinstance(result_set, dict)

    @pytest.mark.parametrize(
        'customer_distance',
        [
            -0.0000001,
            -190,
            -100.901,
            -900,
            -1.3210,
        ]
    )
    def test_negative_customer_distance(self, customer_distance, random_longitude, random_latitude):
        with pytest.raises(ValueError):
            CustomerDb.invite_customers(random_longitude, random_latitude, customer_distance)

    @pytest.mark.parametrize(
        'customer_distance',
        [
            -0.001,
            -190,
            -100.901,
            -900,
            -1.3210,
            None,
            '',
            -1,
            -2,
            -90121,
            {},
            [903, 81],
            {89, 772, 12.00},
            range,
            dict,
            pytest,
            [{'1': ['pqr', 'xyz'], '2': ['abc', 'def']}]
        ]
    )
    def test_invalid_customer_distance(self, customer_distance, random_longitude, random_latitude):
        with pytest.raises(ValueError):
            CustomerDb.invite_customers(random_longitude, random_latitude, customer_distance)

    @pytest.mark.parametrize(
        'longitude',
        [
            -200,
            -1905.00,
            1000,
            181.00,
            180.00000001,
            -180.0000001,
            None,
            '',
            {},
            [903, 81],
            {89, 772, 12.00},
            range,
            dict,
            pytest,
            [{'1': ['pqr', 'xyz'], '2': ['abc', 'def']}]
        ]
    )
    def test_invalid_longitude(self, longitude, random_latitude, random_distance):
        with pytest.raises(ValueError):
            CustomerDb.invite_customers(longitude, random_latitude, random_distance)

    @pytest.mark.parametrize(
        'latitude',
        [
            -91,
            -1905.00,
            92,
            90.0000001,
            -90.000001,
            180.00000001,
            -180.0000001,
            None,
            '',
            -90121,
            {},
            [903, 81],
            {89, 772, 12.00},
            range,
            dict,
            pytest,
            [{'1': ['pqr', 'xyz'], '2': ['abc', 'def']}]
        ]
    )
    def test_invalid_latitude(self, random_longitude, latitude, random_distance):
        with pytest.raises(ValueError):
            CustomerDb.invite_customers(random_longitude, latitude, random_distance)
