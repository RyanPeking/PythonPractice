'''
音乐下载外链
https:music.163.com/song/media/outer/url?id=

1.获取页面源码 https://music.163.com/#/artist?id=6731
2.获取歌曲id以及歌曲名称
3.下载音乐
'''
from tkinter import Tk, Label, Entry, Listbox, Button, END

import os
from urllib import request

from bs4 import BeautifulSoup
import requests


def music_spider():
    url = entry.get()
    # url = 'https://music.163.com/artist?id=6731'
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
        'referer': 'https: // music.163.com /'

    }
    res = requests.get(url, headers=headers).text
    # print(res.text)
    # 创建soup对象
    soup = BeautifulSoup(res, 'lxml')

    # 获取id与歌曲名
    music_dicts = {}
    items = soup.find('ul', {'class':"f-hide"}).find_all('a')
    # print(items)
    for item in items:
        music_id = item.get('href').strip('/song?id=')
        music_name = item.text
        # print(music_id, music_name)
        music_dicts[music_id] = music_name

    # print(music_dicts)
    for song_id in music_dicts:
        song_url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(song_id)
        # print(song_url)

        path = '/home/tlxy/tulingxueyuan/爬虫与实战/数据存储/test/music_163'
        if not os.path.exists(path):
            os.makedirs(path)

        text.insert(END, "loading:{}".format(music_dicts[song_id]))

        text.see(END)

        text.update()

        res = requests.get(url=song_url, headers=headers)
        try:
            request.urlretrieve(song_url, path+'/'+music_dicts[song_id]+'.mp3')
        except:
            print("{}load failed".format(music_dicts[song_id]))
root = Tk()
root.title("网易云音乐下载器")
root.geometry("850x550")
root.geometry("+550+100")

label = Label(root, text="请输入您下载的地址：")

# 定位 pack palce grid
label.grid()

# 设置输入框
entry = Entry(root, width=100)
entry.grid(row=0, column=1)

# 设置列表框
text = Listbox(root, width=110, height=30)
text.grid(row=1, columnspan=2)

# 设置按钮
button1 = Button(root, text="Start", command=music_spider)
button1.grid(row=2, column=0, sticky='s')# sticky对齐方式

# 退出按钮
button2 = Button(root, text="Quit",command=root.quit)
button2.grid(row=2, column=1)

root.mainloop()




