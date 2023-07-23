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
    for _ in range(count):
        for url in urls:
            http_request_serial(url)


@timeit
def http_requests_mutithreading(urls, count):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(http_request_serial, url) for url in urls * count]
        for future in concurrent.futures.as_completed(futures):
            future.result()


@timeit
def http_requests_mutiprocessing(urls, count):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(http_request_serial, url) for url in urls * count]
        for future in concurrent.futures.as_completed(futures):
            future.result()


if __name__ == '__main__':
    urls = sys.argv[1:]

    # http_requests_serial(urls, 100)
    # http_requests_mutithreading(urls, 1000)
    # http_requests_mutiprocessing(urls, 1000)

    """
    Single request ~500ms
    
    Serial
    count  time cpu  mem
    100    52s   8%   0.4%
    
    Multiprocessing - 8
    count  time cpu  mem
    1000   60s  50%  3.2%
    
    Multithreading
    count  time cpu  mem
    1000   45s  50%  0.5%     
    """