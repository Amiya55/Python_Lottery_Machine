import re
import random
import tkinter as tk
from tkinter import messagebox,simpledialog
from tkinter.ttk import *
from tkinter import ttk

 

root = tk.Tk()

root.geometry('500x300')
root.title('夺命摇号器1.2')


style = Style()
style.theme_use('xpnative')


start = tk.StringVar()
end = tk.StringVar()
choice = tk.StringVar()
number = tk.StringVar()
skip = tk.StringVar()
group = tk.StringVar()

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

ttk.Label(page, text='分组抽号，输入分组组数，不填即默认不分组').grid(row=32, column=2, pady=10)
ttk.Entry(page, textvariable=group).grid(row=32, column=3, pady=10)

def get_group():
    group_num = group.get()    #获取分组数量
    return group_num


def skip_num():
    sk = skip.get()     #获取指定跳过数字
    return sk


def lottry():
    st = int(start.get())
    en = int(end.get())        #从tk输入框中获取抽号的起始号和结束号，以及抽号个数
    nu = int(number.get())
    
    return st, en, nu


def prepare_work():
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
    
    # st, en, nu = lottry()
    # st = int(st)
    # en = int(en)
    # nu = int(nu)

    return ignore_list,length


def process():

    ignore_list,length = prepare_work()   #调用函数
    st,en,nu = lottry()

    num_list = []
    i = 0
    while i < nu:
        x = random.randint(st, en)
        if x in num_list or x in ignore_list:
            pass
        else:
            num_list.append(x)
            i += 1
    result = ""
    for index, number in enumerate(num_list, 1):
        result += f"第{index}个，{number}号同学\n"
    messagebox.showinfo("抽号结果", result)


def open_second_window():


    ignore_list,length = prepare_work()
    st,en,nu = lottry()
    # 判断是否分组
    # print(type(get_group()))
    # print(group_list)
    # print(len(group_list))

    if nu > en-st+1-length:
        messagebox.showerror("错误","抽取个数超过人数总数！")



    else:
        is_num = re.match(r'\d+',get_group())
        if not is_num:
            process()  #当分组输入框为空时，直接调用普通抽号
            

        else:
            if 1 == int(get_group()):
                process()    #当分组抽号分组为1时，直接调用普通函数


            else:
                is_average_number = messagebox.askyesno("要平均数吗", "每组人数是否平均?")
                if is_average_number:
                    st, en, nu = lottry()
                    
                    group_num = get_group()
                    count_each_group_member = (nu)//int(group_num)
                    # extra_member = (en+1-st)%int(group_num)

                    
                    ignore_list,length = prepare_work()


                    original_num_list = []
                    i = 0
                    while i < nu:
                        x = random.randint(st, en)
                        if x in original_num_list or x in ignore_list:
                            pass
                        else:
                            original_num_list.append(x)
                            i += 1
                    # print(original_num_list)
                    new_list = []    #初始化父列表
                    count = 1
                    while count <= int(get_group()):     #关键部分，为每个组抽取合适的人数
                        new_list.append(original_num_list[:count_each_group_member])    
                        original_num_list = original_num_list[count_each_group_member:]
                        count+=1
                    # print(original_num_list)
                    for j in range(len(original_num_list)):
                        (new_list[j]).append(original_num_list[j])   #处理平均抽取遗留下的数，将他们逐个添加到各组中

                    result =''
                    for index,end_list in enumerate(new_list,1):
                        result += f'第{index}组，{end_list}号同学\n'
                        # print(f'第{index}组，{end_list}号同学')
                    messagebox.showinfo('抽号结果',result)


                else:    #指定每组人数的情况
                    group_size_input = simpledialog.askstring('','指定每组的人数')
                    if group_size_input:

                        ignore_list,length = prepare_work()
                        
                        st, en, nu = lottry()

                        group_size = re.split(r'\D+',group_size_input)
                        re_group_size = [int(i) for i in group_size]

                        

                        if len(re_group_size) != int(get_group()):
                            messagebox.showerror('错误','请输入正确的值')

                        else:
                            num_list = []
                            i = 0
                            while i < nu:
                                x = random.randint(st, en)
                                if x in num_list or x in ignore_list:
                                    pass
                                else:
                                    num_list.append(x)
                                    i += 1
                            result = ""
                            for index, number in enumerate(num_list, 1):
                                result += f"第{index}个，{number}号同学\n"
                            # print(num_list)

                                                        
                            orginal_num_list = []
                            for i in re_group_size:
                                orginal_num_list.append(num_list[:i])
                                num_list = num_list[i:]
                            result = ''
                            for index, lst in enumerate(orginal_num_list,1):
                                # print(f'第{index}组，{lst}号同学')
                                result +=f'第{index}组，{lst}号同学\n'
                            messagebox.showinfo('分组结果',result)
                            messagebox.askyesno('','是否截图')

                        

        

ttk.Button(page, text='开始抽号', command=open_second_window).grid(row=40, column=3, pady=10)
ttk.Button(page, text='退出', command=page.quit).grid(row=40, column=2, pady=10)

root.mainloop()