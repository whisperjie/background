#!/usr/bin/python3

from tkinter import *

import requests

import json

root=Tk()

entry1=Entry(root,width=50)

entry1.pack()

value1=StringVar()

value2=StringVar()

def query():

    url = "https://aidemo.youdao.com/trans"

    headers = {

        'Accept': 'application/json, text/javascript, */*; q=0.01',

        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',

        'Origin': 'http://ai.youdao.com',

        'Referer': 'http://ai.youdao.com/product-fanyi.s',

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'

    }

    data = {

        'from': 'Auto',

        'to': 'Auto'

    }

    data['q']=entry1.get()

    response = requests.post(url=url, headers=headers, data=data)

    cihui = json.loads(response.content)

    #entry2.select_clear()
    entry2.delete('0','end')

    entry2.insert(0, cihui['web'][0]['value'])

button = Button(root, text="query", command=query).pack()

entry2 = Entry(root,textvariable=value2,width=50)

entry2.pack()

root.mainloop()
