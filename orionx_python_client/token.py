import aiohttp
import asyncio
import json
import logging

from typing import List
from .currency import CEROS
from .queries import get_real_time_token_query


async def get_real_time_token(self, session: aiohttp.ClientSession):
    try:
        logging.info("Getting Real Time Token")
        query_str = get_real_time_token_query()
        payload = {"query": query_str, "variables": {}}
        response = await self.request("POST", "graphql", session, payload)
        token = response["data"]["requestRealtimeToken"]["token"]
        return token
    except Exception as err:
        logging.debug(err)
        raise err
