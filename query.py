from Osu_Data import *
from Osu_Id import *
import tkinter as tk
from tkinter import messagebox
window=tk.Tk()
window.title('OSU rank search！')
window.geometry('390x600')
l=tk.Label(window,text='请输入你的ID:',bg='white',font=('SimSun',14),width=16,height=1,).place(x=10,y=25)
e=tk.Entry(window,width=25,show=None)
e.place(x=10,y=70,anchor='nw')
canvas=tk.Canvas(window,bg= '#9370DB',height=155,width=155)
image_file=tk.PhotoImage(file='Re.png')
image=canvas.create_image(15,15,anchor='nw',image=image_file)
canvas.place(x=380,y=10,anchor='ne')
var=tk.StringVar()
def getmain():
    var = e.get()
    SSS = gethtml(var)
    s_final = getdata(SSS)
    l=tk.Label(window, text=s_final, bg='white', font=('Arial', 14), width=32, height=15).place(x=14, y=175)
b=tk.Button(window,text='开始查询',width=24,height=1,command=getmain).place(x=10,y=120)

window.mainloop()