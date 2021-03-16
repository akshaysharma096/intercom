import json
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
    def invite_customers(longitude: float, latitude: float, max_customer_distance: float) -> list:
        """
        Function to read from the file, and then calculate the the customer which are eligible

        :param longitude: Longitude of the office
        :param latitude: Latitude of the office
        :param max_customer_distance: Max distance under-which customers should be invited.
        :return: A list of customers who are eligible for invitation
        :rtype: list
        """
        source = GeoLocation(longitude, latitude)
        result = dict()
        for customer in CustomerDb.all():
            if is_under_distance(source, customer.geo_location, max_customer_distance):
                result[customer.user_id] = customer
        return [value for (key, value) in sorted(result.items())]
