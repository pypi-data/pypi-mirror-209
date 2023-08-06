from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from base64 import b64encode
import hmac
import hashlib
from datetime import datetime, timezone
import requests
import json
import inspect

class LoginResult(object):
    def __init__(self, access_token, timestamp, signature, success=True, message="") -> None:
        self.access_token = access_token
        self.timestamp = timestamp
        self.signature = signature
        self.success = success
        self.message = message

class LoginClient(object):
    def __init__(self, url, pk_pass, client_id, client_secret, pk_path='', pk='', tz_offset='+07:00') -> None:
        if pk_path == '' and pk == '':
            raise Exception("pk_path or pk is required")
        
        self.url = url
        self.pk_path = pk_path
        self.pk = pk
        self.pk_pass = pk_pass
        self.client_id = client_id
        self.client_secret = client_secret
        self.tz_offset = tz_offset

    def _load_privatekey_(self):
        if self.pk != '':
            return RSA.importKey(self.pk, self.pk_pass)
        return RSA.importKey(open(self.pk_path).read(), self.pk_pass)


    def _generate_signature_(self, data, private_key):
        digest = SHA256.new()
        digest.update(str.encode(data))
        signer = PKCS1_v1_5.new(private_key)
        sign = signer.sign(digest)
        return b64encode(sign).decode()

    def get_token(self):
        local_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000T') + self.tz_offset
        data = "{}|{}".format(self.client_id, local_time)

        private_key = self._load_privatekey_()
        signature = self._generate_signature_(data, private_key)

        req_headers = {
            "X-Mandiri-Key": "{}".format(self.client_id),
            "X-TIMESTAMP": "{}".format(local_time),
            "X-SIGNATURE": "{}".format(signature),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        params = {
            "grant_type":"client_credentials"
        }
        response = requests.post(
            f"{self.url}/openapi/auth/token", headers=req_headers, data=params
        )
        if response.status_code == 200:
            resp_data = response.json()
            return LoginResult(resp_data['accessToken'], local_time, signature)
        else:
            return LoginResult("", local_time, signature, False, response.text)

class TransactionClient(object):
    def __init__(self, client_secret, access_token) -> None:
        self.client_secret = client_secret
        self.access_token = access_token

    def _transaction_signature_(self, client_secret, message):
        signature = hmac.new(
            client_secret.encode(), message.encode(), hashlib.sha512
        ).hexdigest()
        return signature

    def _minified_data_(self, data):
        string = json.dumps(data, separators=(',', ':'))
        return string
    
    def get_signature(self, http_method, url_path, data, local_time):
        jsonBodyRequest = self._minified_data_(data)
        message = "{}:{}:{}:{}:{}".format(
            http_method, url_path, self.access_token, jsonBodyRequest, local_time
        )
        signature = self._transaction_signature_(self.client_secret, message)
        return signature
    