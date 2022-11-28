import requests

class RequestManager:
    def __init__(self, url, key=None, uid=None):
        self.url = url
        self.key = key
        self.uid = uid
        self.header = {'appid': uid,
                      'appkey': key}

    def get_request_data(self, params=None):
        r = requests.get(url=self.url, params=params, headers=self.header)
        r.raise_for_status()
        print(r.status_code, self.url)
        return r.json()

    def post_request_data(self, json=None):
        r = requests.post(url=self.url, json=json, headers=self.header)
        r.raise_for_status()
        print(r.status_code, self.url)
        return r.json()
