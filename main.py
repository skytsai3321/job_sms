import asyncio
import watchlog


async def main():
    print("Hello from job-sms!")


if __name__ == "__main__":
    log_path = 'log/system.log'

    asyncio.run(watchlog.watch_log(log_path))
