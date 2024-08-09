import aiohttp
import asyncio
import time

semaphore = asyncio.Semaphore(10)

async def fetch(session, url):
    async with semaphore:
        async with session.get(url) as response:
            print(f"Status: {response.status}")
            return await response.text()

async def main():
    url = "http://google.com"
    tasks = []

    async with aiohttp.ClientSession() as session:
        for _ in range(100):
            task = asyncio.create_task(fetch(session, url))
            tasks.append(task)

        await asyncio.gather(*tasks)

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time} seconds")
