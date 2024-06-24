#!/usr/bin/env python3
import csv
import math
from typing import List, Dict, Any

def index_range(page, page_size):
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
            dataset = self.dataset()
            assert isinstance(page, int) and page > 0
            assert isinstance(page_size, int) and page_size > 0

            fin, lin = index_range(page, page_size)

            if fin >= len(dataset) or lin < 0:
                return []

            return dataset[fin:lin]
    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
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
