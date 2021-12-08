import requests


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