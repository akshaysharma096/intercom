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
            (GeoLocation(-6.043701, 52.986375), GeoLocation(-10.27699, 51.92893), 310.2771),
            (GeoLocation(35.00875, 61.09623), GeoLocation(-35.97992, -52.33815), 14097.4504),
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
