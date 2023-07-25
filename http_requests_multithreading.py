import concurrent.futures
import sys

from common import http_request
from decorators import timeit


@timeit
def http_requests_mutithreading(urls, count, worker_count=None):
    with concurrent.futures.ThreadPoolExecutor(max_workers=worker_count) as executor:
        futures = [executor.submit(http_request, url) for url in urls * count]
        for future in concurrent.futures.as_completed(futures):
            future.result()


if __name__ == '__main__':
    worker_count = int(sys.argv[1]) or None
    urls = sys.argv[2:]
    http_requests_mutithreading(urls, 1000, worker_count)
