from tkinter import *
import re
import requests

def intepret():
    content = entry1.get() # 拿到第一个输入框里面的内容
    url ="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    data = {
        'i':content,
        'doctype':'json',

    }
    r = requests.post(url,data=data).text
    ret = re.search('"tgt":"(.*?)"}]',r)
    res.set(ret.group(1))



master = Tk()  # 实例化一个对象，master就是一个对象，里面有很多功能

master.geometry('400x100+450+278')  # 设定界面的宽和高 坐标
# master.geometry('')#设定界面的坐标

label1 = Label(master, text='输入内容：', fg='blue', font=('GB2312', 18))
label1.grid(row=0,column=0)

label2 = Label(master, text='结    果：', fg='blue', font=('GB2312', 18))
label2.grid(row=1,column=0)

entry1 = Entry(master,fg='red',font=('GB2312',18))
entry1.grid(row=0,column=1)

res =StringVar()
entry2 = Entry(master,fg='red',font=('GB2312',18),textvariable=res)
entry2.grid(row=1,column=1)

button1 = Button(master,text='翻译', fg='black', font=('GB2312', 18),command=intepret)
button1.grid(row=2,column=0)

button2 = Button(master, text='退出', fg='black', font=('GB2312', 18), command=master.quit)
button2.grid(row=2, column=1,sticky=E)


master.mainloop()  # 这个功能就是让我们图片界面出来