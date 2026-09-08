import asyncio
import time


# ---- async / await basics ----

# async def makes a coroutine - it can pause at await points
# asyncio.run() starts the event loop and runs the coroutine

async def greet():
    print("hello")
    await asyncio.sleep(1)
    print("world")


asyncio.run(greet())


# ---- sequential vs concurrent ----

async def task_seq(name, seconds):
    print(f"{name} started")
    await asyncio.sleep(seconds)
    print(f"{name} done")


async def run_sequential():
    start = time.time()
    await task_seq("A", 2)
    await task_seq("B", 2)
    print(f"sequential total: {time.time() - start:.2f}s")   # ~4s


asyncio.run(run_sequential())


# gather() runs all coroutines at the same time
# total time = longest task, not the sum of all

async def task(name, seconds):
    print(f"{name} started")
    await asyncio.sleep(seconds)
    print(f"{name} done")
    return f"{name} result"


async def run_concurrent():
    start = time.time()
    results = await asyncio.gather(
        task("A", 2),
        task("B", 1),
        task("C", 3),
    )
    print(f"concurrent total: {time.time() - start:.2f}s")   # ~3s
    print("results:", results)


asyncio.run(run_concurrent())


# ---- create_task - start tasks in background ----

async def fetch_data(source, delay):
    await asyncio.sleep(delay)
    return {"source": source, "data": f"response from {source}"}


async def main_tasks():
    t1 = asyncio.create_task(fetch_data("api_1", 2))
    t2 = asyncio.create_task(fetch_data("api_2", 1))
    t3 = asyncio.create_task(fetch_data("api_3", 3))

    print("tasks running in background...")
    await asyncio.sleep(0.1)
    print("doing other work...")

    for r in [await t1, await t2, await t3]:
        print(r)


asyncio.run(main_tasks())


# ---- timeout - cancel if task takes too long ----

async def slow_api():
    await asyncio.sleep(5)
    return "response"


async def main_timeout():
    try:
        async with asyncio.timeout(2):
            result = await slow_api()
            print(result)
    except TimeoutError:
        print("request timed out")


asyncio.run(main_timeout())


# ---- gather with return values ----

async def get_price(item, delay):
    await asyncio.sleep(delay)
    prices = {"laptop": 50000, "phone": 30000, "tablet": 20000}
    return {item: prices[item]}


async def fetch_all_prices():
    results = await asyncio.gather(
        get_price("laptop", 1),
        get_price("phone", 0.5),
        get_price("tablet", 0.8),
    )
    prices = {}
    for r in results:
        prices.update(r)
    print("prices:", prices)


asyncio.run(fetch_all_prices())


# ---- async for - paginated / streamed data ----

async def paginated_api(pages):
    for page in range(1, pages + 1):
        await asyncio.sleep(0.2)
        yield {"page": page, "data": f"items from page {page}"}


async def read_pages():
    async for page in paginated_api(4):
        print(page)


asyncio.run(read_pages())


# ---- async with - async context manager ----
# used for async DB connections, HTTP sessions (e.g. aiohttp)

class AsyncDB:
    async def __aenter__(self):
        print("db: connecting")
        await asyncio.sleep(0.1)
        return self

    async def __aexit__(self, *args):
        print("db: disconnecting")
        await asyncio.sleep(0.1)

    async def query(self, sql):
        await asyncio.sleep(0.2)
        return f"result of: {sql}"


async def use_db():
    async with AsyncDB() as db:
        result = await db.query("SELECT * FROM users")
        print(result)


asyncio.run(use_db())


# ---- practical: scrape 5 urls concurrently ----

async def fake_fetch(url, delay):
    print(f"fetching {url}")
    await asyncio.sleep(delay)
    return {"url": url, "status": 200}


async def scrape_all():
    urls = [
        ("https://site1.com", 1.0),
        ("https://site2.com", 0.5),
        ("https://site3.com", 1.5),
        ("https://site4.com", 0.8),
        ("https://site5.com", 1.2),
    ]

    start = time.time()
    results = await asyncio.gather(
        *[fake_fetch(url, delay) for url, delay in urls]
    )
    print(f"\nscraping done in {time.time() - start:.2f}s")
    for r in results:
        print(r)


asyncio.run(scrape_all())

