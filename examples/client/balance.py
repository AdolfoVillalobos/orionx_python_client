import os
import asyncio
from dotenv import load_dotenv

from orionx_python_client import OrionXClient


async def main():
    api_key = os.getenv("ORIONX_API_KEY")
    secret_key = os.getenv("ORIONX_API_SECRET")
    api_url = os.getenv("ORIONX_API_URL")

    ox = OrionXClient(api_key=api_key, secret_key=secret_key, api_url=api_url)



    resp = ox.get_balance()

    print(resp)


load_dotenv(".env")
asyncio.run(main())
