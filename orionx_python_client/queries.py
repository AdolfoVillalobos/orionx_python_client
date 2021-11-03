def get_order_query(order_id):
    query_str = f"""query {{
                        order(orderId:"{order_id}") {{
                            amount
                            type
                            sell
                            transactions {{
                                id: _id
                                currency{{
                                    code
                                }}
                                pairCurrency {{
                                    code
                                }}
                                amount
                                type
                                price
                                adds
                                commission
                                cost
                                date
                            }}
                        }}
                    }}"""
    return query_str


def get_balance_query():
    query_str = """
        query{
            me {
                wallets {
                    currency{
                        code
                    }
                    balance
                    availableBalance
                    loanLimit
                    loanUsedAmount
                    unconfirmedBalance
                }
            }
        }"""
    return query_str


def get_orders_history_query(page_id):
    query_str = f"""query {{
                        orders (page: {page_id}) {{
                            _id
                            page
                            totalCount
                            totalPages
                            hasNextPage
                            hasPreviousPage
                            items {{
                                _id
                                amount
                                type
                                status
                                transactions {{
                                    _id
                                    currency{{
                                        code
                                    }}
                                    pairCurrency {{
                                        code
                                    }}
                                    amount
                                    type
                                    price
                                    adds
                                    commission
                                    cost
                                    date
                                }}
                            }}
                        }}
                    }}"""
    return query_str


def get_cancel_multiple_orders_query(str_ids: str):
    query = f"""
    mutation{{
        cancelMultipleOrders(ordersIds:{str_ids}){{
            _id
            amount
            limitPrice
            status
            market{{
                name
            }}
        }}
    }}
    """
    return query


def get_cancel_order_query(order_id: str):
    query = f"""
        mutation {{
            cancelOrder(orderId: "{order_id}"){{
                status
            }}
        }}"""
    return query


def get_open_orders_query():
    query_str = """
    query{
        orders(onlyOpen:true){
            items {
                _id
                market{
                    code
                }
                sell
            }
        }
    }
    """
    return query_str


def get_balance_query():
    query_str = """
        query{
            me {
                wallets {
                    currency{
                        code
                    }
                    balance
                    availableBalance
                    loanLimit
                    loanUsedAmount
                    unconfirmedBalance
                }
            }
        }"""
    return query_str


def get_order_status_query(order_id: str):
    query = f"""
        query {{
            order(orderId: "{order_id}"){{
                status
            }}
        }}"""
    return query


def get_new_position_query(
    market_code: str, amount: float, limit_price: float, selling: str
):
    query_str = f"""
        mutation {{
            placeLimitOrder(marketCode: "{market_code}", amount: {amount}, limitPrice: {limit_price}, sell: {selling}){{
                _id
            }}
        }}
    """
    return query_str


def get_real_time_token_query():
    query_str = """
        mutation {
        requestRealtimeToken
        }
        """
    return query_str
