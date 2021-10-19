import asyncio
import logging
import aiohttp
import hashlib
import hmac
import time
import json

from abc import ABC, abstractmethod
from dataclasses import dataclass, Field


@dataclass
class AbstractAPI(ABC):

    api_url: str
    api_key: str
    secret_key: str
    exchange: str

    def __post_init__(self):
        logging.info(
            f"EXCHANGE CLIENT: Credentials for {self.exchange} are ready.")

    async def request(
        self, method: str, path: str, session: aiohttp.ClientSession, payload: dict
    ):
        try:
            timestamp = time.time()
            data = self.get_payload(payload, timestamp)
            signature = self.get_signature(
                payload=payload, endpoint=path, timestamp=timestamp
            )
            headers = self.get_headers(signature, timestamp)
            url = self.api_url + path

            async with session.request(
                method=method,
                url=url,
                headers=headers,
                data=data,
            ) as resp:
                resp.raise_for_status()
                response = await resp.json()
                return self.parse_response(response)
        except Exception as err:
            logging.debug(err)
            raise err

    async def get_public(self, path: str, session: aiohttp.ClientSession, params: dict):
        try:
            url = self.api_url + path
            async with session.get(url=url, params=params) as resp:
                url = resp.url
                response = await resp.json()
                return response
        except Exception as err:
            logging.debug(err)
            raise err

    @abstractmethod
    def get_headers(self, signature):
        pass

    @abstractmethod
    def get_signature(self, payload, endpoint):
        pass

    @abstractmethod
    def get_payload(self, payload):
        pass

    @abstractmethod
    def parse_response(self, response):
        pass


@dataclass
class OrionXAPI(AbstractAPI):
    exchange: str = "orionX"

    def get_headers(self, signature, timestamp):
        headers = {
            "Content-Type": "application/json",
            "X-ORIONX-TIMESTAMP": str(int(timestamp)),
            "X-ORIONX-APIKEY": self.api_key,  # API Key
            "X-ORIONX-SIGNATURE": signature,
        }
        return headers

    def get_signature(self, payload, timestamp):
        body = json.dumps(payload)
        key = bytearray(self.secret_key, "utf-8")
        msg = str(int(timestamp)) + str(body)
        msg = msg.encode("utf-8")
        signature = str(hmac.HMAC(key, msg, hashlib.sha512).hexdigest())
        return signature

    def get_payload(self, payload):
        return json.dumps(payload)

    def parse_response(self, response):
        return response
