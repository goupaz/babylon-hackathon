import os
import requests

from requests.exceptions import HTTPError

CRYPTOWERK_API_KEY = os.getenv("CRYPTOWERK_API_KEY")
CRYPTOWERK_SECRET = os.getenv("CRYPTOWERK_SECRET")


class CryptoWerk():
    base_url = "https://developers.cryptowerk.com/platform/API/v8"
    def __init__(self):
        pass
    def register(self, data_hash):
        register_url = f"{self.base_url}/register"
        data = {"hashes": data_hash}
        response = None

        try:
            response = self.make_request(register_url, data)

        except HTTPError as err:
            print(f"An error occurred. {str(err)}")

        return response

    def verify(self, retrieval_id):
        verify_url = f"{self.base_url}/verify"
        data = {"retrievalId": retrieval_id}
        response = None
        
        try:
            response = self.make_request(verify_url, data)

        except HTTPError as err:
            print(f"An error occurred. {str(err)}")

        return response

    @staticmethod
    def make_request(url, data):
        headers = {
            "accept": "application/json",
            "X-ApiKey": f"{CRYPTOWERK_API_KEY} {CRYPTOWERK_SECRET}"
        }
        response = requests.post(url, params=data, headers=headers)

        if not response.status_code == requests.codes.ok:
            raise HTTPError(response.reason)

        return response.json()

