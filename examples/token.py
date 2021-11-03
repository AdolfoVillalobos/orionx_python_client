import os
import asyncio
import aiohttp
from dotenv import load_dotenv

from orionx_python_client import OrionXClient


async def main():
    api_key = os.getenv("ORIONX_API_KEY")
    secret_key = os.getenv("ORIONX_API_SECRET")
    api_url = os.getenv("ORIONX_API_URL")

    ox = OrionXClient(api_key=api_key, secret_key=secret_key, api_url=api_url)

    async with aiohttp.ClientSession() as session:

        resp = await ox.get_order_status(order_id="123", session=session)

        print(resp)

        resp = await ox.close_order_by_id(order_id="1231", session=session)

        print(resp)


load_dotenv(".env")
asyncio.run(main())
