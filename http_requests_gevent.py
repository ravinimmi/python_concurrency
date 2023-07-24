import gevent
from gevent import monkey; monkey.patch_all()  # noqa: E702

import sys

import requests

from decorators import timeit


@timeit
def http_request_serial(url):
    request = requests.get(url)
    print(f"Response length: {len(request.content)}")


@timeit
def http_requests_gevent(urls, count):
    jobs = [gevent.spawn(http_request_serial, url) for url in urls * count]
    _ = gevent.joinall(jobs, timeout=10)


if __name__ == '__main__':
    urls = sys.argv[1:]
    http_requests_gevent(urls, 1000)
