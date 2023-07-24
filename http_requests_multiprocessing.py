import concurrent.futures
import sys

from common import http_request
from decorators import timeit


@timeit
def http_requests_mutiprocessing(urls, count):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(http_request, url) for url in urls * count]
        for future in concurrent.futures.as_completed(futures):
            future.result()


if __name__ == '__main__':
    urls = sys.argv[1:]
    http_requests_mutiprocessing(urls, 1000)
