from src.models import GeoLocation


class Customer:
    """
        Customer Class, to store information about a customer.
    """

    def __init__(self, user_id: int, name: str, geo_location: GeoLocation):
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

    def __eq__(self, other) -> bool:
        if not isinstance(other, Customer):
            raise ValueError

        return self.user_id == other.user_id

    def __str__(self):
        return "{0} {1} {2}".format(self.user_id, self.name, self.geo_location)
