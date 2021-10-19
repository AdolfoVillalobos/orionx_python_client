import aiohttp
import asyncio
import json
import logging
from typing import List
from .queries import get_cancel_order_query, get_open_orders_query, get_new_position_query, get_cancel_multiple_orders_query


async def close_order_by_id(self, order_id: str, session: aiohttp.ClientSession):
    try:
        logging.info(f"Closing Order {order_id}")
        query_str = get_cancel_order_query(order_id=order_id)
        payload = {"query": query_str, "variables": {}}
        response = await self.client.request("POST", "graphql", session, payload)
        logging.info(response)

        if response["data"].get("cancelOrder", None) == None:
            error_code = response["errors"][0]["details"]["code"]

            if error_code == "concurrent":
                logging.debug(f"Repeated attempt to close {order_id}. ")
                return True

            else:
                logging.debug(error_code)
                return False

        else:
            status = response["data"]["cancelOrder"].get("status")
            if status != "open":
                logging.debug(f"ORder ID {order_id} was closed.")
                return True
            else:
                logging.debug(
                    f"ORder ID {order_id}  COULD NOT BE CLOSED closed.")
                return False

    except Exception as err:
        logging.debug(err)
        return False


async def get_open_orders(self, session: aiohttp.ClientSession):
    try:
        query_str = get_open_orders_query()
        payload = {"query": query_str, "variables": {}}
        response = await self.client.request("POST", "graphql", session, payload)
        logging.info(response)

        if "data" in response:
            ids = {
                order["_id"]: order["market"]["code"]
                for order in response["data"]["orders"]["items"]
            }
            logging.info(f"OPEN ORDERS: {ids}")
            return ids
        return []
    except Exception as err:
        logging.debug(err)
        raise Exception("Could not get open ids")


async def close_orders_by_market(self, market: str, session: aiohttp.ClientSession):
    try:
        logging.info(f"CLOSING ORDERS BY {market}")
        market_orders = await self.get_open_orders_by_market(
            market=market, session=session
        )
        await self.close_orders(list(market_orders.keys()), session=session)
    except Exception as err:
        logging.debug(err)
        raise err


async def get_order_status(self, order_id: str, session: aiohttp.ClientSession):
    try:
        query_str = get_order_status(order_id=order_id)
        payload = {"query": query_str, "variables": {}}
        response = await self.client.request("POST", "graphql", session, payload)
        logging.debug(response)

        if "data" in response:
            status = response["data"]["order"]["status"]
            return status
        return None
    except Exception as err:
        logging.debug(err)
        raise Exception("Could not get Order Status")


async def close_orders(self, order_ids: List[str], session: aiohttp.ClientSession):
    try:
        logging.info(f"CLOSING ORDERS: {order_ids}")
        str_ids = json.dumps(order_ids)
        query_str = get_cancel_multiple_orders_query(str_ids=str_ids)
        payload = {"query": query_str, "variables": {}}
        response = await self.client.request("POST", "graphql", session, payload)

        for order in order_ids:
            status = await self.get_order_status(order_id=order, session=session)
            while status == "open":
                await self.close_order_by_id(order_id=order, session=session)
                status = await self.get_order_status(
                    order_id=order, session=session
                )

            logging.info(f"ORDER {order} has correctly been closed: {status}")
        return response
    except Exception as err:
        logging.debug(err)
        raise Exception(
            "OrionXExchange Error: Could not close orders  {order_ids}")


async def new_position(
    self,
    market_code: str,
    amount: float,
    limit_price: float,
    selling: str,
    session: aiohttp.ClientSession,
):
    try:
        logging.info(f"\tPlaceOrders: Placing New Order. Selling: {selling}")
        first_currency_code, second_currency_code = market_code.split("/")
        limit_price = limit_price * 10 ** CEROS[second_currency_code]
        amount = amount * 10 ** CEROS[first_currency_code]

        query_place_order = get_new_position_query(
            market_code=market_code.replace("/", ""),
            amount=amount,
            limit_price=limit_price,
            selling=selling,
        )

        payload = {"query": query_place_order, "variables": {}}
        response = await self.client.request("POST", "graphql", session, payload)
        logging.info(response)

        if response["data"].get("errors", None) != None:

            error_code = response["errors"][0]["details"]["code"]

            logging.debug(
                f"Failed Order: {amount} {market_code} at {limit_price}. {error_code}"
            )
            if error_code == "insufficientFunds":
                return False
            elif error_code == "amountIsLow":
                return False
            elif error_code == "concurrent":
                await asyncio.sleep(2)
                return False
            else:
                return False

        if response["data"].get("placeLimitOrder", None) == None:

            return False
        else:
            order_id = response["data"].get("placeLimitOrder")["_id"]
            logging.info(
                f"ORDER {order_id} created for market {market_code}. Amount: {amount}, Limit Price: {limit_price}. Selling: {selling}"
            )
            return order_id
    except Exception as err:
        logging.debug(err)
        return False
