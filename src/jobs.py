from functools import lru_cache
import csv


@lru_cache
def read(path: str):
    result = []
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            result.append(row)
    return result
