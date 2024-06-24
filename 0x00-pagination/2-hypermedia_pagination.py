#!/usr/bin/env python3
"""
Implement a get_hyper method that takes the same arguments
(and defaults) as get_page and returns a dictionary containing
the following key-value pairs:

- page_size: the length of the returned dataset page
- page: the current page number
- data: the dataset page (equivalent to the return from the previous task)
- next_page: number of the next page, None if there is no next page
- prev_page: number of the previous page, None if there is no previous page
- total_pages: the total number of pages in the dataset as an integer
"""
import csv
import math
from typing import List, Dict, Any


def index_range(page, page_size):
    """ index_range function"""
    fin = (page - 1) * page_size
    lin = fin + page_size
    return (fin, lin)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get_page function"""
        dataset = self.dataset()
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        fin, lin = index_range(page, page_size)

        if fin >= len(dataset) or lin < 0:
            return []

        return dataset[fin:lin]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
    Returns a dictionary containing information about the dataset page.

    Args:
        page (int): The current page number.
        page_size (int): The number of items per page.

    Returns:
        Dict[str, Any]: A dictionary containing the following key-value pairs:
            - page_size: The length of the returned dataset page.
            - page: The current page number.
            - data: The dataset page.
            - next_page: The number of the next page, None if
            there is no next page.
            - prev_page: The number of the previous page, None if
            there is no previous page.
            - total_pages: The total number of pages in the
            dataset as an integer.
    """
        data = self.get_page(page, page_size)

        total_pages = (len(self.dataset()) + page_size - 1) // page_size

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        result = {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
        return (result)
