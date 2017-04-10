from tkinter import *
import pywapi
from functools import partial



def control_switch(top,flag,city_id,city_name):

   weather_info=pywapi.get_weather_from_weather_com(city_id)

   if(flag==1):
    try:
       temp_la=Label(top,text='Temperature: {} C'.format(weather_info['current_conditions']['temperature']),relief=RAISED,font=('bold',15),bg='white')
       temp_la.place(x=380,y=210)
    except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',15))
       na.place(x=380,y=210)



    try:
       feels_like_la=Label(top,text='Fells like: {} C'.format(weather_info['current_conditions']['feels_like']),relief=RAISED,font=('bold',15),bg='white')
       feels_like_la.place(x=380,y=260)
    except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',15)).place(x=380,y=260)



    try:
       humidity_la=Label(top,text='Humidity: {}'.format(weather_info['current_conditions']['humidity']),bg='white',relief=RAISED,font=('bold',15)).place(x=380,y=310)

    except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',15)).place(x=380,y=310)


    try:
       dew_la=Label(top,text='Current condition: {}'.format(weather_info['current_conditions']['text']),relief=RAISED,font=('bold',15),bg='white').place(x=380,y=460)

    except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',15)).place(x=380,y=460)




    try:
       rise_set__la1=Label(top,text='sunrise {}'.format(weather_info['forecasts'][0]['sunrise']),relief=RAISED,font=('bold',15),bg='white').place(x=380,y=360)


    except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',15)).place(x=380,y=360)





    try:
       visibilty_la=Label(top,text='Visibilty: {}'.format(weather_info['current_conditions']['visibility']),relief=RAISED,font=('bold',15),bg='white').place(x=380,y=410)

    except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',15),bg='white')
       na.place(x=380,y=410)

   ''' try:
       moon_la=Label(top,text='Moon Phase: {}'.format(weather_info['moon_phase']['text']),relief=RAISED,font=('bold',15),bg='white')
       moon_la.place(x=300,y=410)
    except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',15))
       na.place(x=300,y=410)


    try:
       pressure_la=Label(top,text='Pressure: {}'.format(weather_info['barometer']['reading']),relief=RAISED,font=('bold',15),bg='white')
       pressure_la.place(x=300,y=460)
    except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',15))
       na.place(x=300,y=460)'''

   if(flag==2):
     try:
       temp_la=Label(top,text='Temperature: {} C'.format(weather_info['current_conditions']['temperature']),relief=RAISED,font=('bold',15),bg='white')
       temp_la.place(x=700,y=210)
     except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',15))
       na.place(x=700,y=210)



     try:
       feels_like_la=Label(top,text='Fells like: {} C'.format(weather_info['current_conditions']['feels_like']),relief=RAISED,font=('bold',15),bg='white')
       feels_like_la.place(x=700,y=260)
     except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',15)).place(x=700,y=260)



     try:
       humidity_la=Label(top,text='Humidity: {}'.format(weather_info['current_conditions']['humidity']),bg='white',relief=RAISED,font=('bold',15)).place(x=700,y=310)

     except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',15)).place(x=700,y=310)


     try:
       dew_la=Label(top,text='Current condition: {}'.format(weather_info['current_conditions']['text']),relief=RAISED,font=('bold',15),bg='white').place(x=700,y=460)

     except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',15)).place(x=700,y=460)




     try:
       rise_set__la1=Label(top,text='sunrise {}'.format(weather_info['forecasts'][0]['sunrise']),relief=RAISED,font=('bold',15),bg='white').place(x=700,y=360)


     except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',15)).place(x=700,y=360)





     try:
       visibilty_la=Label(top,text='Visibilty: {}'.format(weather_info['current_conditions']['visibility']),relief=RAISED,font=('bold',15),bg='white').place(x=700,y=410)

     except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',15),bg='white')
       na.place(x=700,y=410)

     '''try:
       moon_la=Label(top,text='Moon Phase: {}'.format(weather_info['moon_phase']['text']),relief=RAISED,font=('bold',15),bg='white')
       moon_la.place(x=700,y=410)
     except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',15))
       na.place(x=700,y=410)


     try:
       pressure_la=Label(top,text='Pressure: {}'.format(weather_info['barometer']['reading']),relief=RAISED,font=('bold',15),bg='white')
       pressure_la.place(x=450,y=460)
     except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',15))
       na.place(x=700,y=460)'''


def get_entery1(top,city_name):

    flag=1

    location_ids_of_cities = pywapi.get_location_ids(city_name.get())                #getting location ids from the given entery

    if(len(location_ids_of_cities)==0):
      m=0                                                                                #null statment no siginificane
    else:
        choice={}                                                                           #an empty dictinary
        count=1
        for i in location_ids_of_cities:                                                                  #for every key in loaction id dictionary
            choice[count] = i
            count+=1
        for count in  choice:
             c=Button(top,text=location_ids_of_cities[choice[count]],width=35,height=1,command=partial(control_switch,top,flag,choice[count],location_ids_of_cities[choice[count]]),activebackground='blue')         #creation of buttons
             c.place(x=30,y=120+count*40)




def get_entery2(top,city_name):


    flag=2

    location_ids_of_cities = pywapi.get_location_ids(city_name.get())                #getting location ids from the given entery

    if(len(location_ids_of_cities)==0):
      m=0                                                                             #null statment no siginificane
    else:
        choice={}                                                                           #an empty dictinary
        count=1
        for i in location_ids_of_cities:                                                                  #for every key in loaction id dictionary
            choice[count] = i
            count+=1
        for count in  choice:
             b=Button(top,text=location_ids_of_cities[choice[count]],width=35,height=1,command=partial(control_switch,top,flag,choice[count],location_ids_of_cities[choice[count]]),activebackground='blue')         #creation of buttons
             b.place(x=1100,y=120+count*40)








def compare(x):

    top=Toplevel(x)

    back_ground_image=PhotoImage(file='compare.png')
    label1=Label(top,image=back_ground_image,relief=SUNKEN)     #search frame wallpaper
    label1.place(x=0,y=0,relwidth=1,relheight=1)

    name1=StringVar()
    name2=StringVar()



    entry1=Entry(top,bg='white',bd=8,width=20,textvariable=name1).place(x=50,y=65)
    button1=Button(top,text='GO',width=10,font='20',fg='blue',command= partial(get_entery1,top,name1)).place(x=200,y=65)


    entry2=Entry(top,bg='white',bd=8,textvariable=name2).place(x=1100,y=65)
    button2=Button(top,text='GO',fg='blue',font='20',height=1,width=10,command= partial(get_entery2,top,name2)).place(x=1250,y=65)

    global indicator1
    global indicator2

    indicator1=0
    indicator2=0
    top.geometry('1366x700+-7+-2')
    top.wm_title("------------------------------COMPARE WEATHER----------------------------------- ")
    top.geometry('1366x740')
    x.mainloop()


indicator1=0
indicator2=0
city1=''
city2=''
city_name1=''
city_name2=''
