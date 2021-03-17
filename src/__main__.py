# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>

from tabulate import tabulate

from src.constants import (
    DUBLIN_LATITUDE,
    DUBLIN_LONGITUDE,
    CUSTOMER_DISTANCE
)
from src.db import CustomerDb


def entry_point():
    """
    Main function that is called for calculating the eligible customers around the Dublin Office.

    :return: None
    :rtype: None
    """
    calculate_customers_nearby()


def calculate_customers_nearby():
    """
    Calculates the a set of customers who are eligible for invitation and then tabulates and shows them in a sorted manner

    :return: None
    :rtype: None
    """
    result_set = CustomerDb.invite_customers(DUBLIN_LONGITUDE, DUBLIN_LATITUDE, CUSTOMER_DISTANCE)
    customers = [result_set[key] for key in sorted(result_set.keys())]
    customer_list = [[customer.user_id, customer.name] for customer in customers]
    print(tabulate(customer_list, headers=["ID", "Name"]))


entry_point()
