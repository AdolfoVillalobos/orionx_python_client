import aiohttp


from .queries import get_order_query, get_orders_history_query, get_balance_query


async def get_order(self, order_id: str, session: aiohttp.ClientSession):

    query_str = get_order_query(order_id)
    payload = {"query": query_str, "variables": {}}
    response = await self.request("POST", "graphql", session, payload)

    return response


async def get_orders_history(self, page_id: str, session: aiohttp.ClientSession):
    query_str = get_orders_history_query(page_id=page)
    payload = {"query": query_str, "variables": {}}
    response = await self.request(
        "POST", "graphql", session, payload
    )

    return response


async def get_balance(self, session: aiohttp.ClientSession):
    query_str = get_balance_query()
    payload = {"query": query_str, "variables": {}}
    response = await self.request("POST", "graphql", session, payload)
    return response
