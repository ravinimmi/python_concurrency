import requests
from decorators import timeit


@timeit
def http_request(url):
    request = requests.get(url)
    print(f"Response length: {len(request.content)}")