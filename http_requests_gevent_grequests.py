import sys

import grequests

from decorators import timeit


@timeit
def http_requests_grequests(urls, count):
    requests = (grequests.get(url) for url in urls * count)
    responses = grequests.map(requests)
    for response in responses:
        print(f"Response length: {len(response.content)}")


if __name__ == '__main__':
    urls = sys.argv[1:]
    http_requests_grequests(urls, 1000)
