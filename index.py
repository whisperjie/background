import requests
import os
import json
import time
import win32api
import win32con
import win32gui

def getImgUrl():
    url="https://cn.bing.com/HPImageArchive.aspx?format=js&n=10"
    res=requests.get(url)
    
    myjson=json.loads(res.text)
    #urllist
   
    return myjson['images'][0]['copyright'],myjson["images"][0]['url']
  





def getImg(imagePath,url,imageName):
    #https://cn.bing.com/th?id=OHR.PortlandDawn_ZH-CN6187930845_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp
    myurl="https://cn.bing.com/"+url
    print(myurl)
    res=requests.get(url=myurl)
    imagespicificPath=imagePath+imageName
    print(imagespicificPath)
    
    
    if res.status_code==200:
        with open(imagespicificPath,'wb') as f:
            f.write(res.content)
    else:
        print("获取失败")

def setBackGround(imagePath):
   # 将下载后的图片设置为Windows系统的桌面
    # 打开指定注册表路径
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    # 最后的参数:2拉伸,0居中,6适应,10填充,0平铺
    win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    # 最后的参数:1表示平铺,拉伸居中等都是0
    win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # 刷新桌面
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, imagePath, win32con.SPIF_SENDWININICHANGE)



if __name__ == "__main__":
    imagePath="img/"
    imageName=time.strftime("%Y-%m-%d", time.localtime())+".jpg"
    name, url=getImgUrl()
    print(url,name)
    getImg(imagePath,url,imageName)

    absolutePath=os.path.abspath(imagePath+"/"+imageName)
    print(absolutePath)
    #getImgUrl()
    setBackGround(absolutePath)




