import asyncio
import aiofiles


async def create_file(index):
    filename = f"file_{index}.txt"
    async with aiofiles.open(filename, 'w') as f:
        await f.write(f"This is file number {index}")
    print(f"Created {filename}")

async def main():
    tasks = [create_file(i) for i in range(1, 11)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
