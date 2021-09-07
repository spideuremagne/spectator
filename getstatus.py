import ssl
import urllib
from urllib.error import HTTPError
import json


# use this if you have ephemeral certs from an untrusted CA, otherwise comment out
# ssl._create_default_https_context = ssl._create_unverified_context


def pollHostStatus(host):
    try:
        # change http to https if using...
        url = 'http://' + host + '/announce/payload.json'
        # url = str(host.join('/announce/payload.json'))
        # url = prependUrl.join(url)
        print(url)
        get = urllib.request.Request(url)
        data = urllib.request.urlopen(get)
        payload = json.load(data)
        # print(payload)
        return payload
    except HTTPError:
        raise
