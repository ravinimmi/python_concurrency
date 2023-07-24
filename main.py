import asyncio
import concurrent.futures
import sys

import aiohttp
import requests

from decorators import timeit, timeit_async


@timeit
def http_request(url):
    request = requests.get(url)
    print(f"Response length: {len(request.content)}")


@timeit
def http_requests_serial(urls, count):
    for _ in range(count):
        for url in urls:
            http_request(url)


@timeit
def http_requests_mutithreading(urls, count):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(http_request, url) for url in urls * count]
        for future in concurrent.futures.as_completed(futures):
            future.result()


# @timeit
def http_requests_mutiprocessing(urls, count):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(http_request, url) for url in urls * count]
        for future in concurrent.futures.as_completed(futures):
            future.result()


@timeit_async
async def http_request_coroutine(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"Response length: {len(await response.text())}")


async def http_requests_asyncio_coroutine(urls, count):
    async with asyncio.TaskGroup() as tg:
        for _ in range(count):
            for url in urls:
                tg.create_task(http_request_coroutine(url))


@timeit
def http_requests_asyncio(urls, count):
    asyncio.run(http_requests_asyncio_coroutine(urls, count))


if __name__ == '__main__':
    urls = sys.argv[1:]

    # http_requests_serial(urls, 100)
    # http_requests_mutithreading(urls, 1000)
    # http_requests_mutiprocessing(urls, 1000)
    http_requests_asyncio(urls, 1000)
