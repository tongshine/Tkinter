import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from random import random

root = tk.Tk()
root.geometry('500x300+100+100')
root.title('辞职信')

frame1 = tk.Frame(root)
frame1.pack()

tk.Label(frame1, text='尊敬的各位领导：', padx=30, pady=30).pack(side=tk.LEFT, anchor=tk.N)

img = Image.open('imge/cizhi.jpg')
img = ImageTk.PhotoImage(img)
label_img = tk.Label(frame1, image=img, padx=30, pady=30, bd=0)
label_img.pack(side=tk.LEFT, anchor=tk.N)

tk.Label(frame1, text='辞职人：tongshine', height=25, padx=30, pady=30, bd=0, anchor=tk.S).pack(side=tk.LEFT)

yes = tk.Button(frame1, text='同意', font=('黑体', 18), fg='green', bd=0,command=frame1.pack_forget)#关掉第一个窗体
no = tk.Button(frame1, text='拒绝', font=('黑体', 18), fg='red', bd=0)
yes.place(relx=0.3, rely=0.7, anchor=tk.CENTER)  # 绝对布局
no.place(relx=0.7, rely=0.7, anchor=tk.CENTER)
#创建第二个窗体
frame2 = tk.Frame(root)
frame2.pack()
tk.Label(frame2,
         text='平时学习工作中，\n\n我们经常会接触到一些大佬写的Python工具，\n\n运行起来总会显示出五颜六色的字体，\n\n比如红色代表Error， \n\n黄色代表Warning， \n\n绿色代表Success。',
          font=('楷体',14),padx=30, pady=30, bd=0, anchor=tk.S).pack(side=tk.LEFT)
tk.Button(frame2, text='退出', command=root.quit).place(relx=0.9, rely=0.8)


def on_exit():
    messagebox.showwarning(title='提示', message='此路不通')


root.protocol('WM_DELETE_WINDOW', on_exit)


def move(event):
    no.place(relx=random(), rely=random(), anchor=tk.CENTER)


no.bind('<Enter>', move)

root.mainloop()
