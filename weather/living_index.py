from tkinter import *
import tkinter.messagebox
def out(info):

    top=Toplevel()

    summer=['Sun','Sunny','Fair','Clear']
    rain=['Rain','Rainy','Thunder','Storm']
    cloudy=['Cloudy','Fog','Haze','Mist']

    current=info['current_conditions']['text']
    for k in summer:
        if k in current:
            back_ground_image=PhotoImage(file='living_SUN.png')
            label1=Label(top,image=back_ground_image,relief=SUNKEN)
            label1.place(x=0,y=0,relwidth=1,relheight=1)
        else:
            continue

    for k in rain:
        if k in current:
            back_ground_image=PhotoImage(file='living_rain.png')
            label1=Label(top,image=back_ground_image,relief=SUNKEN)
            label1.place(x=0,y=0,relwidth=1,relheight=1)
        else:
            continue
    for k in cloudy:
        if k in current:
            back_ground_image=PhotoImage(file='living_cloudy.png')
            label1=Label(top,image=back_ground_image,relief=SUNKEN)
            label1.place(x=0,y=0,relwidth=1,relheight=1)
        else:
            continue
    if current=='':
        tkinter.messagebox.showinfo('Living index','Not available')
    top.wm_title("--------------------------------------LIVING INDEX------------------------------------- ")
    top.geometry('1366x768')

    top.geometry('1366x768+-7+0')

    top.mainloop()


def out2(info):

    top=Toplevel()

    summer=['Sun','Sunny','Fair','Clear']
    rain=['Rain','Rainy','Thunder','Storm']
    cloudy=['Cloudy','Fog','Haze','Mist']

    current=info['current_conditions']['text']
    for k in summer:
        if k in current:
            back_ground_image=PhotoImage(file='living_SUN.png')
            label1=Label(top,image=back_ground_image,relief=SUNKEN)
            label1.place(x=0,y=0,relwidth=1,relheight=1)
        else:
            continue

    for k in rain:
        if k in current:
            back_ground_image=PhotoImage(file='living_rain.png')
            label1=Label(top,image=back_ground_image,relief=SUNKEN)
            label1.place(x=0,y=0,relwidth=1,relheight=1)
        else:
            continue
    for k in cloudy:
        if k in current:
            back_ground_image=PhotoImage(file='living_cloudy.png')
            label1=Label(top,image=back_ground_image,relief=SUNKEN)
            label1.place(x=0,y=0,relwidth=1,relheight=1)
        else:
            continue
    if current=='':
        tkinter.messagebox.showinfo('Living index','Not available')
    top.wm_title("--------------------------------------LIVING INDEX------------------------------------- ")
    top.geometry('1366x700+-7+-2')
    top.mainloop()