from tkinter import *
import pywapi
import weather.forecast,weather.living_index,weather.outdoor_index,weather.sports_index

def basic_weather_update_window(weather_info,f,o,s,l):

      top=Toplevel()
      top.wm_title("--------------------------------BASIC WEATHER UPDATE------------------------------ ")
      #background images
      back_ground_image=PhotoImage(file='basic.png')
      label1=Label(top,image=back_ground_image,relief=SUNKEN)     #search frame wallpaper
      label1.place(x=0,y=0,relwidth=1,relheight=1)
      top.geometry('1366x700+-7+-2')

      #information
      try:
       temp_la=Label(top,text=weather_info['current_conditions']['temperature'],bg='white',relief=RAISED,font=('bold',55))
       temp_la.place(x=260,y=150)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',45))
       na.place(x=260,y=150)
      try:
       feels_like_la=Label(top,text=weather_info['current_conditions']['feels_like'],bg='white',relief=RAISED,font=('bold',55))
       feels_like_la.place(x=750,y=150)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',45))
       na.place(x=750,y=150)
      try:
       humidity_la=Label(top,text=weather_info['current_conditions']['humidity'],bg='white',relief=RAISED,font=('bold',45))
       humidity_la.place(x=1250,y=100)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',45))
       na.place(x=1250,y=70)
      try:
       dew_la=Label(top,text=weather_info['current_conditions']['dewpoint'],relief=RAISED,font=('bold',55))
       dew_la.place(x=300,y=480)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',55))
       na.place(x=300,y=550)
      try:
       current_la=Label(top,text=weather_info['current_conditions']['text'],relief=RAISED,font=('bold',30))
       current_la.place(x=480,y=600)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',45))
       na.place(x=620,y=600)
      try:
       current_la=Label(top,text='lat: {}'.format(weather_info['location']['lat']),relief=RAISED,font=('bold',30))
       current_la.place(x=1150,y=500)
       current_la=Label(top,text='lon: {}'.format(weather_info['location']['lon']),relief=RAISED,font=('bold',30))
       current_la.place(x=1150,y=600)
      except:
       na = Label(top,text="NA",relief=RAISED,font=('bold',45))
       na.place(x=1250,y=650)

      status_units=Label(top,text=weather_info['units'],relief=SUNKEN,bd=1,height=1)
      status_units.pack(side=BOTTOM,fill=X)


      if(f==1):
       weather.forecast.forecast(weather_info,o,s,l)
      elif(o==1):
       weather.outdoor_index.out(weather_info,s,l)
      elif(s==1):
       weather.sports_index.out(weather_info,l)
      elif(l==1):
       weather.living_index.out(weather_info)
      else:
       top.mainloop()


def basic_weather_update_window2(weather_info):

      top=Toplevel()
      top.wm_title("--------------------------------BASIC WEATHER UPDATE------------------------------ ")
      #background images
      back_ground_image=PhotoImage(file='basic.png')
      label1=Label(top,image=back_ground_image,relief=SUNKEN)     #search frame wallpaper
      label1.place(x=0,y=0,relwidth=1,relheight=1)
      top.geometry('1366x700+-7+-2')

      #information
      try:
       temp_la=Label(top,text=weather_info['current_conditions']['temperature'],bg='white',relief=RAISED,font=('bold',55))
       temp_la.place(x=260,y=150)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',45))
       na.place(x=260,y=150)
      try:
       feels_like_la=Label(top,text=weather_info['current_conditions']['feels_like'],bg='white',relief=RAISED,font=('bold',55))
       feels_like_la.place(x=750,y=150)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',45))
       na.place(x=750,y=150)
      try:
       humidity_la=Label(top,text=weather_info['current_conditions']['humidity'],bg='white',relief=RAISED,font=('bold',45))
       humidity_la.place(x=1250,y=100)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',45))
       na.place(x=1250,y=70)
      try:
       dew_la=Label(top,text=weather_info['current_conditions']['dewpoint'],relief=RAISED,font=('bold',55))
       dew_la.place(x=300,y=480)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',55))
       na.place(x=300,y=550)
      try:
       current_la=Label(top,text=weather_info['current_conditions']['text'],relief=RAISED,font=('bold',30))
       current_la.place(x=480,y=600)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',45))
       na.place(x=620,y=600)
      try:
       current_la=Label(top,text='lat: {}'.format(weather_info['location']['lat']),relief=RAISED,font=('bold',30))
       current_la.place(x=1150,y=500)
       current_la=Label(top,text='lon: {}'.format(weather_info['location']['lon']),relief=RAISED,font=('bold',30))
       current_la.place(x=1150,y=600)
      except:
       na = Label(top,text="NA",relief=RAISED,font=('bold',45))
       na.place(x=1250,y=650)

      status_units=Label(top,text=weather_info['units'],relief=SUNKEN,bd=1,height=1)
      status_units.pack(side=BOTTOM,fill=X)



      top.mainloop()