# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>

from src.models import GeoLocation


class Customer:
    """
        Customer Class, to store information about a customer.
    """

    def __init__(self, user_id: int, name: str, geo_location: GeoLocation):
        if user_id is None:
            raise ValueError('User Id cannot be blank.')
        if not isinstance(user_id, int):
            raise ValueError('User Id must be an integer.')

        if not isinstance(name, str):
            raise ValueError('Name must be a string.')
        if len(name) == 0:
            raise ValueError('Name cannot be a blank string.')
        if name is None:
            raise ValueError('Name cannot be blank.')

        if geo_location is None:
            raise ValueError('GeoLocation cannot be blank.')
        if not isinstance(geo_location, GeoLocation):
            raise ValueError('GeoLocation must be a valid object.')

        self._user_id = user_id
        self._name = name
        self._geo_location = geo_location

    @property
    def user_id(self):
        return self._user_id

    @property
    def name(self):
        return self._name

    @property
    def geo_location(self):
        return self._geo_location

    def __str__(self):
        return "{0} {1} {2}".format(self.user_id, self.name, self.geo_location)
