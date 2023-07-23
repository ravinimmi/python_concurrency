import concurrent.futures
import sys

import requests

from decorators import timeit


@timeit
def http_request_serial(url):
    request = requests.get(url)
    print(f"Response length: {len(request.content)}")


@timeit
def http_requests_serial(urls, count):
    for url in urls:
        for _ in range(count):
            http_request_serial(url)


@timeit
def http_requests_mutithreading(urls, count):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(http_request_serial, url) for url in urls] * count
        for future in concurrent.futures.as_completed(futures):
            future.result()


if __name__ == '__main__':
    urls = sys.argv[1:]
    print(urls)

    # http_requests_serial(urls, 20)
    http_requests_mutithreading(urls, 100)
