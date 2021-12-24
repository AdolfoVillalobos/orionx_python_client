# OrionX GraphQL API Client for Python

This is a lightweight library that works as a client to the OrionX GraphQL API.

Currently supported APIs:
1.  Placing and canceling limit orders.
2.  Retrieving information about user's wallets.


## Instalation

```bash
pip install orionx-python-client

# Using Poetry
poetry add orionx-python-client@latest
```
## OrionX Api Documentation

http://docs.orionx.com

## GraphQL APIS:

Usage Examples:

```python

import os
import asyncio
import logging
from dotenv import load_dotenv

from orionx_python_client import OrionXClient
logging.basicConfig(
    level=logging.INFO, format="%(levelname)s:%(asctime)s:%(message)s\n\t"
)


def main():
    api_key = os.getenv("ORIONX_API_KEY")
    secret_key = os.getenv("ORIONX_API_SECRET")
    api_url = os.getenv("ORIONX_API_URL")

    ox = OrionXClient(api_key=api_key, secret_key=secret_key, api_url=api_url)

    try:

        # Opening position in BTC/USDT market.
        o1 = ox.new_position(market_code="BTC/USDT", amount=0.0006,
                               limit_price=60000, selling="true")
        logging.info(o1)
        
        # Opening position in BTC/CLP market.
        o2 = ox.new_position(market_code="BTC/CLP", amount=0.0006, limit_price=60000000, selling="true")
        logging.info(o2)

        # Closing Open Positions 
        resp = ox.close_orders(order_ids=[o1, o2])

        print(resp)
    except Exception as err:
        logging.error(err)

if __name__ == "__main__":
    load_dotenv(".env")
    main()

```



