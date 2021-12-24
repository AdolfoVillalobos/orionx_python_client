import os
import asyncio
import logging
from dotenv import load_dotenv

from orionx_python_client import OrionXClient
logging.basicConfig(
    level=logging.INFO, format="%(levelname)s:%(asctime)s:%(message)s\n\t"
)


async def main():
    api_key = os.getenv("ORIONX_API_KEY")
    secret_key = os.getenv("ORIONX_API_SECRET")
    api_url = os.getenv("ORIONX_API_URL")

    ox = OrionXClient(api_key=api_key, secret_key=secret_key, api_url=api_url)
    logging.info(ox)

    try:

        o1 = ox.new_position(market_code="BTC/USDT", amount=0.0006,
                               limit_price=60000, selling="true")
        logging.info(o1)
        
        o2 = ox.new_position(market_code="BTC/CLP", amount=0.0006, limit_price=60000000, selling="true")
        logging.info(o2)

        resp = ox.close_orders(order_ids=[o1, o2])

        print(resp)
    except Exception as err:
        logging.error(err)

load_dotenv(".env")
asyncio.run(main())
