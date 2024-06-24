#!/usr/bin/env python3
def index_range(page, page_size):
    fin = (page - 1) * page_size
    lin = fin + page_size
    return (fin, lin)
