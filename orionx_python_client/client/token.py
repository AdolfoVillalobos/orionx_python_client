import logging

from ..queries import get_real_time_token_query


def get_real_time_token(self):
    try:
        logging.info("Getting Real Time Token")
        query_str = get_real_time_token_query()
        payload = {"query": query_str, "variables": {}}
        response = self.post(path="graphql", payload=payload)
        token = response["data"]["requestRealtimeToken"]["token"]
        return token
    except Exception as err:
        logging.debug(err)
        raise err
