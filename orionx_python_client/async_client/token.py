import aiohttp
import logging

from orionx_python_client.queries import get_real_time_token_query


async def get_real_time_token(self, session: aiohttp.ClientSession):
    try:
        logging.info("Getting Real Time Token")
        query_str = get_real_time_token_query()
        payload = {"query": query_str, "variables": {}}
        response = await self.post(path="graphql", payload=payload, session=session)
        token = response["data"]["requestRealtimeToken"]["token"]
        return token
    except Exception as err:
        logging.debug(err)
        raise err
