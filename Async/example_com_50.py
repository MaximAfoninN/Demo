import aiohttp
import asyncio
import aiofiles


async def fetch(session, url, semaphore):
    async with semaphore:
        async with session.get(url) as response:
            status = response.status
            return status


async def write_status_to_file(status, file):
    async with aiofiles.open(file, 'a') as f:
        await f.write(f"Status: {status}\n")


async def make_requests(url, num_requests, max_concurrent_requests, output_file):
    semaphore = asyncio.Semaphore(max_concurrent_requests)
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(num_requests):
            task = asyncio.create_task(fetch(session, url, semaphore))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)

        for status in responses:
            await write_status_to_file(status, output_file)

        assert len(responses) == num_requests


async def main():
    url = "https://example.com/"
    num_requests = 50
    max_concurrent_requests = 10
    output_file = "statuses.txt"

    await make_requests(url, num_requests, max_concurrent_requests, output_file)


if __name__ == "__main__":
    asyncio.run(main())
