import os
import asyncio
import logging
import aiohttp
from dotenv import load_dotenv

from orionx_python_client import AsyncOrionXClient
logging.basicConfig(
    level=logging.INFO, format="%(levelname)s:%(asctime)s:%(message)s\n\t"
)


async def main():
    api_key = os.getenv("ORIONX_API_KEY")
    secret_key = os.getenv("ORIONX_API_SECRET")
    api_url = os.getenv("ORIONX_API_URL")

    ox = AsyncOrionXClient(api_key=api_key, secret_key=secret_key, api_url=api_url)
    logging.info(ox)

    async with aiohttp.ClientSession() as session:

            o1 = await ox.new_position(market_code="BTC/USDT", amount=0.0002,
                                limit_price=60000, selling="true", session=session)
            logging.info(o1)
            
            o2 = await ox.new_position(market_code="BTC/CLP", amount=0.0002, limit_price=60000000, selling="true", session=session)
            logging.info(o2)

            resp = await ox.close_orders(order_ids=[o1, o2], session=session)

            print(resp)

load_dotenv(".env")
asyncio.run(main())
