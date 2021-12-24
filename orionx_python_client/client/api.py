import logging
import hashlib
import hmac
import time
import json
import requests

from typing import Dict
from pydantic import BaseModel, Field


class BaseAPI(BaseModel):
    api_url: str
    api_key: str
    secret_key: str
    exchange: str
    class Config:
        arbitrary_types_allowed = True

    def post(self, path: str, payload: Dict):
        try:
            timestamp = time.time()
            data = self.get_payload(payload=payload)
            signature = self.get_signature(
                payload=payload, timestamp=timestamp)
            headers = self.get_headers(
                signature=signature, timestamp=timestamp)
            url = self.api_url + path

            response = requests.post(url=url, headers=headers, data=data, timeout=10)
            response.raise_for_status()
            return json.loads(response.text)

        except Exception as err:
            logging.error(err)
            raise err

    def get(self, path: str, payload: Dict):
        try:
            timestamp = time.time()
            data = self.get_payload(payload=payload)
            signature = self.get_signature(
                payload=payload, timestamp=timestamp)
            headers = self.get_headers(
                signature=signature, timestamp=timestamp)
            url = self.api_url + path


            response = requests.get(url=url, headers=headers, data=data, timemout=10)
            response.raise_for_status()
            return response

        except Exception as err:
            logging.error(err)
            raise err

    def get_headers(self, signature: str):
        pass

    def get_signature(self, payload: str, timestamp: int):
        pass

    def get_payload(self, payload: Dict):
        pass

    def parse_response(self, response: Dict):
        pass


class OrionXAPI(BaseAPI):
    exchange: str = "orionX"

    def get_headers(self, signature, timestamp) -> Dict:
        try:
            headers = {
                "Content-Type": "application/json",
                "X-ORIONX-TIMESTAMP": str(int(timestamp)),
                "X-ORIONX-APIKEY": self.api_key,  # API Key
                "X-ORIONX-SIGNATURE": signature,
            }
            return headers
        except Exception as err:
            logging.error(f"Could not get headers")
            raise err

    def get_signature(self, payload: Dict, timestamp: int) -> str:
        try:
            body = json.dumps(payload)
            key = bytearray(self.secret_key, "utf-8")
            msg = str(int(timestamp)) + str(body)
            msg = msg.encode("utf-8")
            signature = str(hmac.HMAC(key, msg, hashlib.sha512).hexdigest())
            return signature
        except Exception as err:
            logging.error(f"Could not get signature")
            raise err

    def get_payload(self, payload) -> str:
        return json.dumps(payload)

    def parse_response(self, response):
        return response
