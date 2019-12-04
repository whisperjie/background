import win32api
import win32con
import win32gui
import os
import random

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
    imagepathlist=[]
    for i in os.listdir(imagePath):
        index=os.path.abspath(imagePath+"/"+i)
        imagepathlist.append(index)

    size=len(imagepathlist)-1
    index=random.randint(0,size)
    setBackGround(imagepathlist[index])
