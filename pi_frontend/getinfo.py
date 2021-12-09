import requests
import json

def get_announcement():
    res = []
    r = requests.get(' http://127.0.0.1:8000/viewannounce/')
    dic = r.json()
    for i in dic.values():
        res.append(i)

    return res


def get_scheudule(sid):
    res = []
    url = 'http://127.0.0.1:8000/viewcourse/' + sid
    r = requests.get(url=url)
    dic = r.json()
    for i in dic.values():
        res.append(i)

    return res

def send_bluez(load):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    url = 'http://127.0.0.1:8000/attend/'
    r = requests.post(url,data=json.dumps(load),headers=headers)
