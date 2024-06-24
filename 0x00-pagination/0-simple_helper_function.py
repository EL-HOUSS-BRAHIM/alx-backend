#!/usr/bin/env python3
"""
    index_range:
    function that takes two integer arguments page and page_size
    arguments:
    page: the page number, page_size: the number of items per page
    page_size: the size of the page
    Returns: a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters
"""


def index_range(page, page_size):
    """ index_range function"""
    fin = (page - 1) * page_size
    lin = fin + page_size
    return (fin, lin)
