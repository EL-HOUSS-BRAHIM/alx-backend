import csv
import math
from typing import List

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
