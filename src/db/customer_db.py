# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>

import json
from collections import defaultdict
from typing import Generator

from src.constants import DATA_STORE_PATH
from src.models import GeoLocation, Customer
from src.utils.distance import is_under_distance


class CustomerDb:

    @staticmethod
    def all() -> Generator:
        with open(DATA_STORE_PATH, 'r') as file:
            for line in file.readlines():
                json_data = json.loads(line)
                geo_location = GeoLocation(
                    float(json_data['longitude']),
                    float(json_data['latitude'])
                )
                customer_obj = Customer(
                    json_data['user_id'],
                    json_data['name'],
                    geo_location
                )
                yield customer_obj

    @staticmethod
    def invite_customers(longitude: float, latitude: float, max_customer_distance: float) -> dict:
        """
        Function to read from the file, and then calculate the the customer which are eligible

        :param longitude: Longitude of the office
        :param latitude: Latitude of the office
        :param max_customer_distance: Max distance under-which customers should be invited.
        :return: A dictionary with id as key - of customers who are eligible for invitation
        :rtype: dict
        """
        if longitude is None:
            raise ValueError('Longitude cannot be blank.')

        if latitude is None:
            raise ValueError('Latitude cannot be blank.')

        if not isinstance(longitude, float) and not isinstance(longitude, int):
            raise ValueError('Longitude must be a numerical value.')

        if not isinstance(latitude, float) and not isinstance(latitude, int):
            raise ValueError('Latitude must be a numerical value.')

        if not isinstance(max_customer_distance, float) and not isinstance(max_customer_distance, int):
            raise ValueError('Max Customer Distance must be a numerical value.')

        if max_customer_distance < 0:
            raise ValueError('Max Customer Distance cannot be less than 0.')

        source = GeoLocation(longitude, latitude)
        # Take of duplicate IDs
        result = defaultdict(list)
        for customer in CustomerDb.all():
            if is_under_distance(source, customer.geo_location, max_customer_distance):
                result[customer.user_id].append(customer)
        return result
