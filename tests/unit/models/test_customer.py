# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>

import random
import string

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

    @pytest.mark.parametrize(
        'customer_obj, user_id',
        [
            (Customer(901, 'Ronaldo', GeoLocation(-9.742744, 51.999447)), 901),
            (Customer(178, 'Roger Waters', GeoLocation(-7.11167, 53.74452)), 178)
        ]
    )
    def test_customer_user_id(self, customer_obj, user_id):
        assert customer_obj.user_id == user_id

    @pytest.mark.parametrize(
        'customer_obj, name',
        [
            (Customer(901, 'Ronaldo', GeoLocation(-9.742744, 51.999447)), 'Ronaldo'),
            (Customer(178, 'Roger Waters', GeoLocation(-7.11167, 53.74452)), 'Roger Waters')
        ]
    )
    def test_customer_name(self, customer_obj, name):
        assert customer_obj.name == name

    @pytest.mark.parametrize(
        'customer_obj, geolocation',
        [
            (Customer(901, 'Ronaldo', GeoLocation(-9.742744, 51.999447)), GeoLocation(-9.742744, 51.999447)),
            (Customer(178, 'Roger Waters', GeoLocation(-7.11167, 53.74452)), GeoLocation(-7.11167, 53.74452)),
            (Customer(903, 'Jim Waters', GeoLocation(-72.11167, 44.74452)), GeoLocation(-72.11167, 44.74452))
        ]
    )
    def test_customer_geo_location(self, customer_obj, geolocation):
        assert isinstance(customer_obj.geo_location, GeoLocation)
        assert customer_obj.geo_location == geolocation

    @pytest.mark.parametrize(
        'customer_id',
        [
            None,
            'abc',
            'random-string',
            '',
            pytest,
            range,
            (),
            (5, 9, 10),
            {},
            {90, 43, 901},
            dict,
            pytest,
            [56, 901],
            [{'abc': 1, 'efg': 2, 'lmo': 3}],
            {'1': 903, '2': ['xyz']}
        ]
    )
    def test_invalid_customer_id(self, customer_id, random_name):
        with pytest.raises(ValueError):
            Customer(customer_id, random_name, GeoLocation(-9.742744, 51.999447))

    @pytest.mark.parametrize(
        'customer_name',
        [
            None,
            123,
            8.001,
            '',
            (),
            (5, 9, 10),
            {},
            {90, 43, 901},
            range,
            dict,
            float,
            pytest,
            [56, 901],
            [{'abc': 1, 'efg': 2, 'lmo': 3}],
            {'1': 903, '2': ['xyz']}
        ]
    )
    def test_invalid_customer_name(self, customer_name):
        random_id = random.randint(500, 999)
        with pytest.raises(ValueError):
            Customer(random_id, customer_name, GeoLocation(-9.742744, 51.999447))

    @pytest.mark.parametrize(
        'geolocation',
        [
            None,
            123,
            8.001,
            '',
            (),
            (5, 9, 10),
            {},
            {90, 43, 901},
            range,
            dict,
            float,
            pytest,
            [{'abc': 1, 'efg':  2, 'lmo': 3}],
            [56, 901],
            {'1': 903, '2': ['xyz']}
        ]
    )
    def test_invalid_customer_geolocation(self, geolocation, random_name):
        random_id = random.randint(500, 999)
        with pytest.raises(ValueError):
            Customer(random_id, random_name, geolocation)
