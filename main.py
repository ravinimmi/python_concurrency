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



if __name__ == '__main__':
    urls = sys.argv[1:]
    print(urls)

    http_requests_serial(urls, 10)
