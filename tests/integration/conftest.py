# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>

import pytest


@pytest.fixture(scope='module')
def expected_customers_id_for_100kms():
    return [4, 5, 6, 8, 11, 12, 13, 15, 17, 23, 24, 26, 29, 30, 31, 39]


@pytest.fixture(scope='module')
def expected_invited_customers():
    return b'  ID  Name\n----  -----------------\n   4  Ian Kehoe\n   5  Nora Dempsey\n   6  Theresa Enright\n   8  Eoin Ahearn\n  11  Richard Finnegan\n  12  Christina McArdle\n  13  Olive Ahearn\n  15  Michael Ahearn\n  17  Patricia Cahill\n  23  Eoin Gallagher\n  24  Rose Enright\n  26  Stephen McArdle\n  29  Oliver Ahearn\n  30  Nick Enright\n  31  Alan Behan\n  39  Lisa Ahearn\n'