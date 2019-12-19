import requests
import json

def getUrls():
    url="http://gank.io/api/data/%E7%A6%8F%E5%88%A9/10/1"
    r=requests.get(url)
    #print(r.status_code)
    #print(r.content)
    myjson=json.loads(r.content)
    return myjson["results"]


if __name__ == "__main__":
    pass