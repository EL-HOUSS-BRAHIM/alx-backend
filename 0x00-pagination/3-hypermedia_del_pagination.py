#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns a dictionary with pagination information"""
        assert index is None or (isinstance(
            index, int) and index >= 0), "Invalid index"
        assert isinstance(
            page_size, int) and page_size > 0, "Invalid page_size"

        if index is None:
            index = 0

        start_index = index
        end_index = start_index + page_size
        data = self.dataset()[start_index:end_index]

        next_index = end_index if end_index < len(self.dataset()) else None

        result = {
            "index": start_index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }

        return result
