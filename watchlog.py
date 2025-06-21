import asyncio
from watchfiles import awatch


async def watch_log(file_path):
    async for changes in awatch(file_path):
        print(changes)


if __name__ == "__main__":
    asyncio.run(watch_log("log/system.log"))
