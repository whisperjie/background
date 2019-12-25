import requests
import json
import threading
import os
def getUrls(i):
    url="http://gank.io/api/data/%E7%A6%8F%E5%88%A9/10/"+str(i)
    r=requests.get(url)
    #print(r.status_code)
    #print(r.content)
    myjson=json.loads(r.content)
    return myjson["results"]


def getImg(imagePath,url,imageName):
    #https://cn.bing.com/th?id=OHR.PortlandDawn_ZH-CN6187930845_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp
    #myurl="https://cn.bing.com/"+url
    for i in os.listdir(imagePath): 
        if i==imageName+'.jpg':
            print(imageName+"已下载")
            return
    res=requests.get(url=url)
    imagespicificPath=imagePath+imageName+".jpg"
    if res.status_code==200:
        with open(imagespicificPath,'wb') as f:
            f.write(res.content)
            print(imageName+"下载完成")
    else:
        print("获取失败")




if __name__ == "__main__":
    imagePath = "meizi/"
    images=getUrls(1)
    for k in images:
        #print(k)
        t=threading.Thread(target=getImg,args=(imagePath,k['url'],k['_id']))
        t.start()
        print(k['_id']+"下载中。。。。。。。。。。。。。。。。。。。")
        