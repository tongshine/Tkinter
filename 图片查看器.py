import glob
import tkinter as tk
from  PIL  import Image, ImageTk
root = tk.Tk()
root.geometry('700x500')
root.title('图片查看器')

photos = glob.glob('imge/*.jpg') #用正则匹配到文件
photos = [ImageTk.PhotoImage(Image.open(photo)) for  photo in photos]#转二进制，转TmageeTk对象
num = len(photos)

page= 0
photo_label = tk.Label(root,image=photos[page],width=700,height=400)#创建图片标签
photo_label.pack()

def page_add():
    global page,num
    page=page+1
    print(page)
    if num ==page:#转第一张
        page=0
    photo_label.configure(image=photos[page])
    pagename.configure(text='第{}页'.format(page+1))#避开第0页


def page_minus():
    global page,num
    page= page-1
    if page ==-1:#转最后一张
        page=num-1
    photo_label.configure(image=photos[page])
    pagename.configure(text='第{}页'.format(page+1))
button_frame=tk.Frame(root) #创建一个容器装按钮
button_frame.pack()
tk.Button(button_frame,text = '下一张',command=page_add).pack(side=tk.LEFT)
tk.Button(button_frame,text = '上一张',command=page_minus).pack(side=tk.RIGHT)
pagename=tk.Label(root, text='第{}页'.format(page+1))
pagename.pack()

root.mainloop()
