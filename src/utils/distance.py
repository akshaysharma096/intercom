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
    return degrees * math.pi / 180


def calculate_geo_distance(location1: GeoLocation, location2: GeoLocation) -> float:
    """
    Calculates the distance between two points on earth, using the great-circle distance formula

    :param location1: Geolocation Object
    :param location2: Geolocation Object
    :return: Total distance in kilo-meters between the two Geolocation objects
    :rtype: float
    """
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

    distance_between_points = calculate_geo_distance(source, target)
    return distance_between_points <= limit
