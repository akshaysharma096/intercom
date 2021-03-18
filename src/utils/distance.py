# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>

import math

from src.constants import EARTH_RADIUS
from src.models.geo_location import GeoLocation


def degree_to_radians(degrees: float) -> float:
    """
    Converts a value in degrees to radians

    :param degrees: Value in degrees
    :return: Value in radians
    :rtype: float
    """
    if degrees is None:
        raise ValueError('Degrees cannot be empty.')

    if not isinstance(degrees, float) and not isinstance(degrees, int):
        raise ValueError('Degrees must be a numerical value.')

    return degrees * math.pi / 180


def calculate_geo_distance(location1: GeoLocation, location2: GeoLocation) -> float:
    """
    Calculates the distance between two points on earth, using the great-circle distance formula

    :param location1: Geolocation Object
    :param location2: Geolocation Object
    :return: Total distance in kilo-meters between the two Geolocation objects
    :rtype: float
    """
    if location1 is None:
        raise ValueError('Location-1 cannot be empty.')
    if location2 is None:
        raise ValueError('Location-2 cannot be empty.')

    if not isinstance(location1, GeoLocation) or not isinstance(location2, GeoLocation):
        raise ValueError('Both of the locations must be GeoLocation objects.')

    delta = degree_to_radians(location1.longitude - location2.longitude)
    radian_latitude_1 = degree_to_radians(location1.latitude)
    radian_latitude_2 = degree_to_radians(location2.latitude)

    computed_value = math.sin(radian_latitude_1) * math.sin(radian_latitude_2) + math.cos(radian_latitude_1) * math.cos(
        radian_latitude_2) * math.cos(
        delta
    )

    return EARTH_RADIUS * math.acos(computed_value)


def is_under_distance(source: GeoLocation, target: GeoLocation, limit: float) -> bool:
    """
    Calculates whether a target point is under a specific distance from the source.

    :param source: The source location from where the search is performed.
    :param target: The target point we want to analyse its within the range.
    :param limit: The distance in kilometers that defines the space the point must belong to.
    :return: Whether the distance between two points on earth, under the limit
    :rtype: bool
    """
    if not isinstance(source, GeoLocation):
        raise ValueError('Source location must be a Geolocation object.')

    if not isinstance(target, GeoLocation):
        raise ValueError('Target location must be a Geolocation object.')

    if not isinstance(limit, float) and not isinstance(limit, int):
        raise ValueError('Max limit must be numerical in nature.')

    if limit < 0:
        raise ValueError('Limit cannot be less than zero.')

    distance_between_points = calculate_geo_distance(source, target)
    return distance_between_points <= limit
