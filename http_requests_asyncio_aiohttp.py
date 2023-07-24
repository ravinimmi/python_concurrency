import asyncio
import sys

import aiohttp

from decorators import timeit, timeit_async


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
    http_requests_asyncio(urls, 1000)
