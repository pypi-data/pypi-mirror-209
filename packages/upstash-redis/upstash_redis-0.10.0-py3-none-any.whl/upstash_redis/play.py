from upstash_py.client import Redis
from asyncio import run


redis = Redis(
    url="https://funky-grubworm-30552.upstash.io",
    token="AXdYASQgNmVmN2RhOTQtMmM4OS00ZDEyLThhNzYtNDdmYjQyNGZlODRiOTZlYTgzZjJiODc4NDAwMzlhN2UyMzk5YTcwYzEzZGE=",
)


async def main():
    async with redis:
        await redis.set("a", "b")
        print(await redis.get("a"))


run(main())


from typing import Optional

param: Optional[int] = 5

param: int | None