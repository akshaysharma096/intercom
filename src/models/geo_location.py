# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>

import math


class GeoLocation:
    """
        GeoLocation class which abstracts a single point over earth.
    """

    def __init__(self, longitude: float, latitude: float):
        if not isinstance(longitude, float) and not isinstance(longitude, int):
            raise ValueError('Longitude has to be a numerical value.')

        if not isinstance(latitude, float) and not isinstance(latitude, int):
            raise ValueError('Latitude has to be a numerical value.')

        if longitude is None:
            raise ValueError('Longitude cannot be empty.')

        if latitude is None:
            raise ValueError('Latitude cannot be empty.')

        if not (-180 <= longitude <= 180):
            raise ValueError('Longitude must be between -180 and 180.')

        if not (-90 <= latitude <= 90):
            raise ValueError('Latitude must be between -90 and 90.')

        self._latitude = latitude
        self._longitude = longitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def latitude(self):
        return self._latitude

    def __eq__(self, other) -> bool:
        if not isinstance(other, GeoLocation):
            raise ValueError

        return math.isclose(self.latitude, other.latitude, rel_tol=1e-5
                            ) and math.isclose(self.longitude, other.longitude, rel_tol=1e-5)

    def __str__(self) -> str:
        return "({0}, {1})".format(self.longitude, self.latitude)
