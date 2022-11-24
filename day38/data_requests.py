import requests


def get_request_data(url, params=None, headers=None):
    r = requests.get(url=url, params=params, headers=headers)
    r.raise_for_status()
    return r.json()


def post_request_data(url, json=None, headers=None):
    r = requests.post(url=url, json=json, headers=headers)
    r.raise_for_status()
    print(r.status_code, url)
    return r.json()
