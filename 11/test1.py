from tkinter import *
import requests


#爬虫的业务逻辑
def get_content():
    ip = ip_input.get()
    url = 'https://www.ipip.net/ip/{}.html'.format(ip)
    html= requests.get(url=url)
    print(html)

#构建窗口
tk = Tk()
#设置标题
tk.title('ip地址')
#输入框
ip_input=Entry(tk,width=40)
#构建一个回显列表
display_info = Listbox(tk,width=50,height=10)
#按钮事件
result_button=Button(tk,coomand=get_content(),text='查询')


#程序入口
if __name__ =='__main__':
    # 显示 界面
    ip_input.pack()
    display_info.pack()
    result_button.pack()
    # 运行
    tk.mainloop()