import requests
from collections import namedtuple
from typing import List

Result = namedtuple('Result', 'category, id url title description')


def search_by_keyword(keyword: str) -> List[Result]:

    url = f'https://search.talkpython.fm/api/search?q={keyword}'

    resp = requests.get(url)
    print(f'The status is {resp.status_code}')

    resp.raise_for_status()

    results = resp.json()["results"]

    results_list = [Result(**result) for result in results]

    return results_list

