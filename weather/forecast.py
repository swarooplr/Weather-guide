import pywapi
from tkinter import *
import weather.outdoor_index,weather.living_index,weather.sports_index

def forecast(info,o,s,l,):

    top=Toplevel()
    back_ground_image=PhotoImage(file='forecast.png')
    label=Label(top,image=back_ground_image,relief=SUNKEN)
    label.place(x=0,y=0,relwidth=1,relheight=1)

    for i in range(1,5):
        date=Label(top,text=info['forecasts'][i]['date'],relief=RAISED,font=('bold',15),bg='white')
        date.place(x=150+250*i,y=120)
        day=Label(top,text=info['forecasts'][i]['day_of_week'],relief=RAISED,font=('bold',15),bg='white')
        day.place(x=150+250*i,y=150)
        sunrise=Label(top,text=info['forecasts'][i]['sunrise'],relief=RAISED,font=('bold',15),bg='white')
        sunrise.place(x=150+255*i,y=200)
        sunset=Label(top,text=info['forecasts'][i]['sunset'],relief=RAISED,font=('bold',15),bg='white')
        sunset.place(x=150+255*i,y=250)
        humidity=Label(top,text=info['forecasts'][i]['night']['humidity'],relief=RAISED,font=('bold',15),bg='white')
        humidity.place(x=170+255*i,y=300)
        min_temp=Label(top,text=info['forecasts'][i]['high'],relief=RAISED,font=('bold',15),bg='white')
        min_temp.place(x=150+250*i,y=385)
        max_temp=Label(top,text=info['forecasts'][i]['low'],relief=RAISED,font=('bold',15),bg='white')
        max_temp.place(x=150+250*i,y=443)


    top.geometry('1366x740+-7+0')

    if(o==1):
        weather.outdoor_index.out(info,s,l)
    elif(s==1):
        weather.sports_index.out(info,l)
    elif(l==1):
        weather.living_index.out(info)
    else:
     top.mainloop()












def forecast2(info):

    top=Toplevel()
    back_ground_image=PhotoImage(file='forecast.png')
    label=Label(top,image=back_ground_image,relief=SUNKEN)
    label.place(x=0,y=0,relwidth=1,relheight=1)

    for i in range(1,5):
        date=Label(top,text=info['forecasts'][i]['date'],relief=RAISED,font=('bold',15),bg='white')
        date.place(x=150+250*i,y=170)
        day=Label(top,text=info['forecasts'][i]['day_of_week'],relief=RAISED,font=('bold',15),bg='white')
        day.place(x=150+250*i,y=210)
        sunrise=Label(top,text=info['forecasts'][i]['sunrise'],relief=RAISED,font=('bold',15),bg='white')
        sunrise.place(x=160+255*i,y=260)
        sunset=Label(top,text=info['forecasts'][i]['sunset'],relief=RAISED,font=('bold',15),bg='white')
        sunset.place(x=160+255*i,y=320)
        humidity=Label(top,text=info['forecasts'][i]['night']['humidity'],relief=RAISED,font=('bold',15),bg='white')
        humidity.place(x=180+255*i,y=380)
        min_temp=Label(top,text=info['forecasts'][i]['high'],relief=RAISED,font=('bold',15),bg='white')
        min_temp.place(x=150+250*i,y=485)
        max_temp=Label(top,text=info['forecasts'][i]['low'],relief=RAISED,font=('bold',15),bg='white')
        max_temp.place(x=150+250*i,y=543)

    top.geometry('1366x700+-7+-2')
    top.mainloop()







