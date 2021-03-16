import json
from typing import Generator

from src.constants import DATA_STORE_PATH
from src.models import GeoLocation, Customer
from src.utils.distance import is_under_distance
from collections import defaultdict


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
    def invite_customers(longitude: float, latitude: float, max_customer_distance: float):
        source = GeoLocation(longitude, latitude)
        result = dict()
        for customer in CustomerDb.all():
            if is_under_distance(source, customer.geo_location, max_customer_distance):
                result[customer.id] = customer.name

        for key in sorted(result.keys()):
            print(result[key])
