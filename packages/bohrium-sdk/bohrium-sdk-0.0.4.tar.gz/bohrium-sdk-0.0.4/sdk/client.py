import requests
import os
import json
import urllib
import getpass
import time

class RequestInfoException(Exception):
    pass

class Client:
    def __init__(self, 
                 debug=False,
                 email="",
                 password="",
                 base_url="https://bohrium.dp.tech",
                 token="",
                 config_file_location='~/.brmconfig',
                 use_config_file=False):
        self.debug = debug
        self.debug = os.getenv('LBG_CLI_DEBUG_PRINT', debug)
        self.config = {}
        self.accesskey = ""
        config_file_location_expand = os.path.expanduser(config_file_location)
        file_data = {}
        self.token = ""
        self.user_id = None
        if use_config_file:
            if os.path.exists(config_file_location_expand):
                with open(config_file_location_expand, "r") as f:
                    file_data = json.loads(f.read())

        else:
            self.config["email"] = email
            self.config["password"] = password
            self.base_url = base_url
        if token is not None:
            self.token = token
        else:
            self._login()
        

    def post(self, url, data=None, header=None, params=None, retry=5):
        return self._req('POST', url, data=data, header=header, params=params, retry=retry)

    def get(self, url, data=None, header=None, params=None, retry=5):
        return self._req('GET', url, data=data, header=header, params=params, retry=retry)

    def _req(self, method, url, data=None, header=None, params=None, retry=5):
        short_url = url
        url = urllib.parse.urljoin(self.base_url, short_url)
        if header is None:
            header = {}
        if self.token:
            header['Authorization'] = f'Bearer {self.token}'
        header['bohr-client'] = f'utility:0.0.2'
        resp_code = None
        for i in range(retry):
            resp = None
            if method == 'GET':
                resp = requests.get(url, params=params, headers=header)
            if method == 'POST':
                resp = requests.post(url=url, json=data, params=params, headers=header)
            if self.debug:
                print(resp.text)
            resp_code = resp.status_code
            if not resp.ok:
                if self.debug:
                    print(f"retry: {i}, statusCode: {resp.status_code}")
                try:
                    result = resp.json()
                    err = result.get("error")
                except:
                    pass
                time.sleep(0.1 * i)
                continue
            result = resp.json()
            if result.get('model', '') == 'gpt-35-turbo':
                return result['choices'][0]['message']['content']
            elif result['code'] == 0:
                return result.get('data', {})
            else:
                err = result.get("message") or result.get("error")
                break
        raise RequestInfoException(resp_code, short_url, err)

    def get_token(self):
        self.login()
        return self.token


    def login(self):
        email = input("Please enter Bohrium Account Email: ")
        password = getpass.getpass(prompt="Please enter password: ")
        post_data = {
            'username': email,
            'password': password
        }
        resp = self.post('/account_gw/login', post_data)
        self.token = resp['token']
        print("Login successfully!")

    def generate_accesskey(self, name="default"):
        post_data = {
            "name": name
        }
        resp = self.post(url="https://bohrium.dp.tech/bohrapi/v1/ak/add", data=post_data)
        self.accesskey = resp["accessKey"]
        return resp


    def chat(self, prompt, temperature=0):
        post_data = {
            "messages":[{"role":"user","content":f"{prompt}"}],
            "stream":False,
            "model":"gpt-3.5-turbo",
            "temperature":temperature,
            "presence_penalty":0
        }
        
        url = f"https://openapi.dp.tech/openapi/v1/chat/complete?accessKey={self.accesskey}"
        resp = requests.post(url=url, json=post_data).json()
        return resp['choices'][0]['message']['content']
