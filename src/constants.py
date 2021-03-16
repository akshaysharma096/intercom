"""
    Project wide constants
"""
import os

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)

DATA_STORE_PATH = os.path.join(dir_path, "store/customers.txt")
EARTH_RADIUS = 6378.0
CUSTOMER_DISTANCE = 100.0
DUBLIN_LATITUDE = 53.339428
DUBLIN_LONGITUDE = -6.257664
