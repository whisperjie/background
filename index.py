import requests
import json
import re
import time
import threading
import os


def getImgUrl():
    url="https://cn.bing.com/HPImageArchive.aspx?format=js&n=10"
    res=requests.get(url)
    myjson=json.loads(res.text)['images']
    imgs=[]
    for v in myjson:
        image={}
        pattern = re.compile(".*?(?=\\()")
        image['name']=pattern.match(v['copyright']).group()
        image['url']=v['url']
        imgs.append(image)
    return imgs
  





def getImg(imagePath,url,imageName):
    #https://cn.bing.com/th?id=OHR.PortlandDawn_ZH-CN6187930845_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp
    myurl="https://cn.bing.com/"+url
    for i in os.listdir(imagePath):
        
        if i==imageName+'.jpg':
            print(imageName+"已下载")
            return
    res=requests.get(url=myurl)
    imagespicificPath=imagePath+imageName+'.jpg'
    if res.status_code==200:
        with open(imagespicificPath,'wb') as f:
            f.write(res.content)
            print(imageName+"下载完成")
    else:
        print("获取失败")
    return



if __name__ == "__main__":
    imagePath="img/"
    imgs=getImgUrl()
    for k  in imgs:
        t=threading.Thread(target=getImg,args=(imagePath,k['url'],k['name']))
        t.start()
        print(k['name']+"下载中。。。。。。。。。。。。。。。。。。。")
        
    






