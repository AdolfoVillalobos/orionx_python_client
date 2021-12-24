
from ..queries import get_order_query, get_orders_history_query, get_balance_query


def get_order(self, order_id: str):

    query_str = get_order_query(order_id)
    payload = {"query": query_str, "variables": {}}
    response = self.post(path="graphql", payload=payload)

    return response


def get_orders_history(self, page_id: str):
    query_str = get_orders_history_query(page_id=page_id)
    payload = {"query": query_str, "variables": {}}
    response = self.post(
        path="graphql", payload=payload
    )

    return response


def get_balance(self):
    query_str = get_balance_query()
    payload = {"query": query_str, "variables": {}}
    response = self.post(path="graphql", payload=payload)
    return response
