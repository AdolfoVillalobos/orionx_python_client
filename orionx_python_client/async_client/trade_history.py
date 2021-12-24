import aiohttp
from orionx_python_client.queries import get_order_query, get_orders_history_query, get_balance_query


async def get_order(self, order_id: str, session: aiohttp.ClientSession):

    query_str = get_order_query(order_id)
    payload = {"query": query_str, "variables": {}}
    response = await self.post(path="graphql", payload=payload, session=session)

    return response


async def get_orders_history(self, page_id: str, session: aiohttp.ClientSession):
    query_str = get_orders_history_query(page_id=page_id)
    payload = {"query": query_str, "variables": {}}
    response = await self.post(
        path="graphql", payload=payload, session=session
    )

    return response


async def get_balance(self, session: aiohttp.ClientSession):
    query_str = get_balance_query()
    payload = {"query": query_str, "variables": {}}
    response = await self.post(path="graphql", payload=payload, session=session)
    return response
