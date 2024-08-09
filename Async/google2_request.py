import aiohttp
import asyncio
import time

semaphore = asyncio.Semaphore(10)

async def fetch(session, url):
    async with semaphore:
        async with session.get(url) as response:
            print(f"Status: {response.status}")
            return await response.text()

async def rate_limited_fetch(session, url, delay):
    await fetch(session, url)
    await asyncio.sleep(delay)

async def main():
    url = "http://google.com"
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(100):
            # Рассчитываем задержку, чтобы ограничить 10 запросов в секунду
            delay = i // 10
            task = asyncio.create_task(rate_limited_fetch(session, url, delay))
            tasks.append(task)

        await asyncio.gather(*tasks)

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time} seconds")
