import ssl
import urllib
from socket import timeout
from urllib.error import URLError, HTTPError
import json


ssl._create_default_https_context = ssl._create_unverified_context


def pollHostStatus(host):
    try:
        # try https first
        url = 'https://' + host + '/announce/payload.json'
        print(url)
        get = urllib.request.Request(url)
        data = urllib.request.urlopen(get, timeout=5)
        payload = json.load(data)
        return payload

    # if https is not it, try http
    except urllib.error.URLError as e:
        print('hit timeout!')
        print(e.__dict__)
        if isinstance(e.reason, ConnectionRefusedError):
            url = 'http://' + host + '/announce/payload.json'
            print(url)
            get = urllib.request.Request(url)
            data = urllib.request.urlopen(get, timeout=5)
            payload = json.load(data)
            return payload
        elif isinstance(e.reason, timeout):
            url = 'http://' + host + '/announce/payload.json'
            print(url)
            get = urllib.request.Request(url)
            data = urllib.request.urlopen(get, timeout=5)
            payload = json.load(data)
            return payload


    except HTTPError:
        pass
