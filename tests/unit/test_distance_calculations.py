# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>

import pytest

from src.models import GeoLocation
from src.utils.distance import degree_to_radians, calculate_geo_distance, is_under_distance


class TestDistanceCalculations:
    """
        Unit tests to test the distance calculation module.
    """

    @pytest.mark.parametrize(
        'input_degrees, output_radians',
        [(90, 1.570796), (60, 1.04719755), (35, 0.610865), (176.90, 3.087487)]
    )
    def test_degree_to_radians(self, input_degrees, output_radians):
        assert degree_to_radians(input_degrees) == pytest.approx(output_radians)

    @pytest.mark.parametrize(
        'geo_distance_1, geo_distance_2, actual_distance',
        [
            (GeoLocation(-6.043701, 52.986375), GeoLocation(-10.27699, 51.92893), 310.277),
            (GeoLocation(35.00875, 61.09623), GeoLocation(-35.97992, -52.33815), 14097.450),
            (GeoLocation(56.49281, 16.81308), GeoLocation(59.97301, 43.04321), 2938.425)
        ]
    )
    def test_calculate_geo_distance(self, geo_distance_1, geo_distance_2, actual_distance):
        assert calculate_geo_distance(geo_distance_1, geo_distance_2) == pytest.approx(actual_distance)

    @pytest.mark.parametrize(
        'source_geo_location, final_geo_location, limit, is_under_limit_or_not',
        [
            (GeoLocation(-6.043701, 52.986375), GeoLocation(-10.27699, 51.92893), 300, False),
            (GeoLocation(-6.043701, 52.986375), GeoLocation(-10.27699, 51.92893), 311.98, True),
            (GeoLocation(-30.34382, -25.56970), GeoLocation(-108.48439, 58.83732), 3000, False),
            (GeoLocation(-30.34382, -25.56970), GeoLocation(-108.48439, 58.83732), 11784, False),
            (GeoLocation(-30.34382, -25.56970), GeoLocation(-108.48439, 58.83732), 11784.759, True)
        ]
    )
    def test_is_under_distance(self, source_geo_location, final_geo_location, limit, is_under_limit_or_not):
        assert is_under_distance(source_geo_location, final_geo_location, limit) == is_under_limit_or_not

    @pytest.mark.parametrize(
        'invalid_degrees',
        [
            None,
            '',
            {},
            [8922, 00],
            range,
            {23, 9, 901, 31.3},
            'abcdef',
            range,
            pytest,
            (),
            (90, 9.01),
            [{1: 45, 90: ['pqr']}]
        ]
    )
    def test_invalid_degrees(self, invalid_degrees):
        with pytest.raises(ValueError):
            degree_to_radians(invalid_degrees)

    @pytest.mark.parametrize(
        'invalid_degrees',
        [
            None,
            '',
            {},
            [8922, 00],
            range,
            GeoLocation,
            {23, 9, 901, 31.3},
            'abcdef',
            range,
            pytest,
            (),
            (90, 9.01),
            [{1: 45, 90: ['pqr']}]
        ]
    )
    def test_invalid_degrees_to_radians(self, invalid_degrees):
        with pytest.raises(ValueError):
            degree_to_radians(invalid_degrees)

    @pytest.mark.parametrize(
        'location1',
        [
            None,
            '',
            {},
            [8922, 00],
            range,
            -123,
            -190.00,
            -180.0001,
            -180.001,
            GeoLocation,
            {23, 9, 901, 31.3},
            'abcdef',
            range,
            pytest,
            (),
            ('abc', '190', 90.00, -1),
            (90, 9.01),
            [{1: 45, 90: ['pqr']}]
        ]
    )
    def test_invalid_location1_calculate_geo_distance(self, location1, random_longitude, random_latitude):
        with pytest.raises(ValueError):
            location2 = GeoLocation(random_longitude, random_latitude)
            calculate_geo_distance(location1, location2)

    @pytest.mark.parametrize(
        'location2',
        [
            None,
            '',
            {},
            [8922, 00],
            range,
            -123,
            -190.00,
            -180.0001,
            -180.001,
            GeoLocation,
            {23, 9, 901, 31.3},
            'abcdef',
            range,
            pytest,
            (),
            ('abc', '190', 90.00, -1),
            (90, 9.01),
            [{1: 45, 90: ['pqr']}]
        ]
    )
    def test_invalid_location2_calculate_geo_distance(self, location2, random_longitude, random_latitude):
        with pytest.raises(ValueError):
            location1 = GeoLocation(random_longitude, random_latitude)
            calculate_geo_distance(location1, location2)

    @pytest.mark.parametrize(
        'source',
        [
            None,
            '',
            {},
            [8922, 00],
            range,
            -123,
            -190.00,
            -180.0001,
            -180.001,
            GeoLocation,
            {23, 9, 901, 31.3},
            'abcdef',
            range,
            pytest,
            (),
            ('abc', '190', 90.00, -1),
            (90, 9.01),
            [{1: 45, 90: ['pqr']}]
        ]
    )
    def test_invalid_source_is_under_distance(self, source, random_longitude, random_latitude, random_distance):
        with pytest.raises(ValueError):
            target = GeoLocation(random_longitude, random_latitude)
            is_under_distance(source, target, random_distance)

    @pytest.mark.parametrize(
        'random_distance',
        [
            None,
            '',
            {},
            [8922, 00],
            range,
            -0.00000001,
            -123,
            -190.00,
            -180.0001,
            -180.001,
            GeoLocation,
            {23, 9, 901, 31.3},
            'abcdef',
            range,
            pytest,
            (),
            ('abc', '190', 90.00, -1),
            (90, 9.01),
            [{1: 45, 90: ['pqr']}]
        ]
    )
    def test_invalid_limit_is_under_distance(self, random_geolocations, random_distance):
        with pytest.raises(ValueError):
            source, target = random_geolocations
            is_under_distance(source, target, random_distance)
