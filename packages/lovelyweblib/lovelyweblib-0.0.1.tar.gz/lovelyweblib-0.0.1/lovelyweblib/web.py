import aiohttp
import asyncio


async def fetch_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response


def get_single_page_sync(url):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(fetch_page(url))


def get_multiple_pages1(urls):
    async def fetch_pages():
        for url in urls:
            yield await fetch_page(url)

    return fetch_pages()


def get_multiple_pages2(urls):
    async def fetch_pages(queue):
        for url in urls:
            queue.put_nowait(await fetch_page(url))

    q = asyncio.Queue()
    asyncio.ensure_future(fetch_pages(q))
    return q
