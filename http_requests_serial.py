import sys

from common import http_request
from decorators import timeit


@timeit
def http_requests_serial(urls, count):
    for _ in range(count):
        for url in urls:
            http_request(url)


if __name__ == '__main__':
    urls = sys.argv[1:]
    http_requests_serial(urls, 100)
