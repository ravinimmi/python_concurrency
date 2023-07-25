import asyncio
import sys
from concurrent.futures import ThreadPoolExecutor

import aiohttp

from decorators import timeit_async


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


def inner_loop(urls, count):
    asyncio.run(http_requests_asyncio_coroutine(urls, count))


@timeit_async
async def http_requests_asyncio(urls, count):
    n = 4
    loop = asyncio.get_event_loop()
    pool = ThreadPoolExecutor(max_workers=n)
    tasks = [loop.run_in_executor(pool, inner_loop, urls, count // n) for _ in range(n)]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    urls = sys.argv[1:]
    asyncio.run(http_requests_asyncio(urls, 1000))
