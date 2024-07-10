import re
import random
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import ttk
 

root = tk.Tk()

root.geometry('500x300')
root.title('夺命摇号器1.1')


style = Style()
style.theme_use('xpnative')


start = tk.StringVar()
end = tk.StringVar()
choice = tk.StringVar()
number = tk.StringVar()
skip = tk.StringVar()

page = ttk.Frame(root)
page.pack()

ttk.Label(page).grid(row=0, column=0)

ttk.Label(page, text='输入从几号开始').grid(row=2, column=2, pady=10)
ttk.Entry(page, textvariable=start).grid(row=2, column=3, pady=10)

ttk.Label(page, text='输入到几号结束').grid(row=8, column=2, pady=10)
ttk.Entry(page, textvariable=end).grid(row=8, column=3, pady=10)

ttk.Label(page, text='输入抽取的个数').grid(row=16, column=2, pady=10)
ttk.Entry(page, textvariable=number).grid(row=16, column=3, pady=10)

ttk.Label(page, text='输入指定跳过的号码，记得随便用什么符号隔开，空格也行').grid(row=24, column=2, pady=10)
ttk.Entry(page, textvariable=skip).grid(row=24, column=3, pady=10)

def skip_num():
    sk = skip.get()     #获取指定跳过数字
    return sk

def lottry():
    st = start.get()
    en = end.get()        #从tk输入框中获取抽号的起始号和结束号，以及抽号个数
    nu = number.get()
    return st, en, nu

def show_result():
    sk = skip_num()     #sk是一个字符串
    skip_list = re.split(r'\D+', sk)  # 使用正则表达式分隔字符串，\D+ 表示匹配一个或多个非数字字符
    ignore_list = []   #建立跳过号码的列表
    for i in skip_list:    
        try:
            x = int(i)
            ignore_list.append(x)
        except ValueError:
            pass
    length = len(ignore_list)
    
    st, en, nu = lottry()
    s = int(st)
    e = int(en)
    n = int(nu)
    
    if e - s + 1 >= n + length:
        num_list = []
        i = 0
        while i < n:
            x = random.randint(s, e)
            if x in num_list or x in ignore_list:
                pass
            else:
                num_list.append(x)
                i += 1
        result = ""
        for index, number in enumerate(num_list, 1):
            result += f"第{index}个，{number}号同学\n"
        messagebox.showinfo("抽号结果", result)
    else:
        messagebox.showerror("错误","抽取个数超过人数总数！")

ttk.Button(page, text='开始抽号', command=show_result).grid(row=32, column=3, pady=10)
ttk.Button(page, text='退出', command=page.quit).grid(row=32, column=2, pady=10)

root.mainloop()