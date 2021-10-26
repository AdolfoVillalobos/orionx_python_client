from .api import OrionXAPI


class OrionXClient(OrionXAPI):

    def __init__(self, api_key=None, secret_key=None, api_url=None):

        super().__init__(api_key=api_key, api_url=api_url, secret_key=secret_key)

    # Get Toek

    from orionx_python_client.token import get_real_time_token

    # Trade History
    from orionx_python_client.trade_history import get_order
    from orionx_python_client.trade_history import get_balance
    from orionx_python_client.trade_history import get_orders_history

    # Order Status
    from orionx_python_client.orders import get_open_orders
    from orionx_python_client.orders import get_open_orders_by_market
    from orionx_python_client.orders import get_order_status

    # Close Orders
    from orionx_python_client.orders import close_order_by_id
    from orionx_python_client.orders import close_orders_by_market
    from orionx_python_client.orders import close_orders

    # New Position
    from orionx_python_client.orders import new_position
