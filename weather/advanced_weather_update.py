from tkinter import *
import pywapi
import weather.sports_index,weather.living_index,weather.outdoor_index,weather.forecast

def advanced_weather_update_window(weather_info,f,o,s,l):

      top=Toplevel()
      back_ground_image=PhotoImage(file='advance.png')
      label1=Label(top,image=back_ground_image,relief=SUNKEN)     #search frame wallpaper
      label1.place(x=0,y=0,relwidth=1,relheight=1)
      top.geometry('1366x700+-7+-2')
      #information
      try:
       temp_la=Label(top,text=weather_info['current_conditions']['temperature'],bg='white',relief=RAISED,font=('bold',30))
       temp_la.place(x=225,y=105)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',30))
       na.place(x=225,y=105)
      try:
       feels_like_la=Label(top,text=weather_info['current_conditions']['feels_like'],bg='white',relief=RAISED,font=('bold',30))
       feels_like_la.place(x=560,y=105)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',30))
       na.place(x=560,y=105)
      try:
       humidity_la=Label(top,text=weather_info['current_conditions']['humidity'],bg='white',relief=RAISED,font=('bold',30))
       humidity_la.place(x=890,y=80)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',30))
       na.place(x=890,y=60)
      try:
       dew_la=Label(top,text=weather_info['current_conditions']['dewpoint'],bg='white',relief=RAISED,font=('bold',30))
       dew_la.place(x=200,y=340)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',30))
       na.place(x=200,y=340)
      try:
       current_la=Label(top,text=weather_info['current_conditions']['text'],bg='white',relief=RAISED,font=('bold',25))
       current_la.place(x=350,y=400)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',30))
       na.place(x=430,y=400)
      try:
       loc_la=Label(top,text='lat: {}'.format(weather_info['location']['lat']),bg='white',relief=RAISED,font=('bold',25))
       loc_la.place(x=860,y=320)
       loc_la1=Label(top,text='lon: {}'.format(weather_info['location']['lon']),bg='white',relief=RAISED,font=('bold',25))
       loc_la1.place(x=860,y=405)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',35))
       na.place(x=870,y=350)
      try:
       max_min_la1=Label(top,text='{}'.format(weather_info['forecasts'][0]['high']),bg='white',relief=RAISED,font=('bold',25))
       max_min_la1.place(x=1155,y=73)
       max_min_la2=Label(top,text='{}'.format(weather_info['forecasts'][0]['low']),bg='white',relief=RAISED,font=('bold',25))
       max_min_la2.place(x=1155,y=170)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',35))
       na.place(x=1150,y=75)
      try:
       rise_set__la1=Label(top,text='{}'.format(weather_info['forecasts'][0]['sunrise']),bg='white',relief=RAISED,font=('bold',20))
       rise_set__la1.place(x=850,y=530)
       rise_set__la2=Label(top,text='{}'.format(weather_info['forecasts'][0]['sunset']),bg='white',relief=RAISED,font=('bold',20))
       rise_set__la2.place(x=750,y=630)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',35))
       na.place(x=850,y=670)
      try:
       wind_la=Label(top,text=weather_info['current_conditions']['wind']['speed'],bg='white',relief=RAISED,font=('bold',35))
       wind_la.place(x=560,y=550)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',35))
       na.place(x=560,y=550)
      try:
       visibilty_la=Label(top,text=weather_info['current_conditions']['visibility'],bg='white',relief=RAISED,font=('bold',30))
       visibilty_la.place(x=200,y=550)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',30))
       na.place(x=200,y=550)
      try:
       moon_la=Label(top,text=weather_info['moon_phase']['text'],bg='white',relief=RAISED,font=('bold',35))
       moon_la.place(x=1120,y=600)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',35))
       na.place(x=1200,y=600)
      try:
       pressure_la=Label(top,text=weather_info['barometer']['reading'],bg='white',relief=RAISED,font=('bold',35))
       pressure_la.place(x=1210,y=350)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',35))
       na.place(x=1210,y=350)

       #status bar containing units
      status_units=Label(top,text=weather_info['units'],bg='white',relief=SUNKEN,bd=1,height=1)
      status_units.pack(side=BOTTOM,fill=X)

      top.wm_title("----------------------------ADVANCE WEATHER UPDATE---------------------- ")
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



def advanced_weather_update_window2(weather_info):

      top=Toplevel()
      back_ground_image=PhotoImage(file='advance.png')
      label1=Label(top,image=back_ground_image,relief=SUNKEN)     #search frame wallpaper
      label1.place(x=0,y=0,relwidth=1,relheight=1)
      top.geometry('1366x700+-7+-2')
      #information
      try:
       temp_la=Label(top,text=weather_info['current_conditions']['temperature'],bg='white',relief=RAISED,font=('bold',30))
       temp_la.place(x=225,y=105)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',30))
       na.place(x=225,y=105)
      try:
       feels_like_la=Label(top,text=weather_info['current_conditions']['feels_like'],bg='white',relief=RAISED,font=('bold',30))
       feels_like_la.place(x=560,y=105)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',30))
       na.place(x=560,y=105)
      try:
       humidity_la=Label(top,text=weather_info['current_conditions']['humidity'],bg='white',relief=RAISED,font=('bold',30))
       humidity_la.place(x=890,y=80)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',30))
       na.place(x=890,y=60)
      try:
       dew_la=Label(top,text=weather_info['current_conditions']['dewpoint'],bg='white',relief=RAISED,font=('bold',30))
       dew_la.place(x=200,y=340)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',30))
       na.place(x=200,y=340)
      try:
       current_la=Label(top,text=weather_info['current_conditions']['text'],bg='white',relief=RAISED,font=('bold',25))
       current_la.place(x=350,y=400)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',30))
       na.place(x=430,y=400)
      try:
       loc_la=Label(top,text='lat: {}'.format(weather_info['location']['lat']),bg='white',relief=RAISED,font=('bold',25))
       loc_la.place(x=860,y=320)
       loc_la1=Label(top,text='lon: {}'.format(weather_info['location']['lon']),bg='white',relief=RAISED,font=('bold',25))
       loc_la1.place(x=860,y=405)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',35))
       na.place(x=870,y=350)
      try:
       max_min_la1=Label(top,text='{}'.format(weather_info['forecasts'][0]['high']),bg='white',relief=RAISED,font=('bold',25))
       max_min_la1.place(x=1155,y=73)
       max_min_la2=Label(top,text='{}'.format(weather_info['forecasts'][0]['low']),bg='white',relief=RAISED,font=('bold',25))
       max_min_la2.place(x=1155,y=170)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',35))
       na.place(x=1150,y=75)
      try:
       rise_set__la1=Label(top,text='{}'.format(weather_info['forecasts'][0]['sunrise']),bg='white',relief=RAISED,font=('bold',20))
       rise_set__la1.place(x=850,y=530)
       rise_set__la2=Label(top,text='{}'.format(weather_info['forecasts'][0]['sunset']),bg='white',relief=RAISED,font=('bold',20))
       rise_set__la2.place(x=750,y=630)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',35))
       na.place(x=850,y=670)
      try:
       wind_la=Label(top,text=weather_info['current_conditions']['wind']['speed'],bg='white',relief=RAISED,font=('bold',35))
       wind_la.place(x=560,y=550)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',35))
       na.place(x=560,y=550)
      try:
       visibilty_la=Label(top,text=weather_info['current_conditions']['visibility'],bg='white',relief=RAISED,font=('bold',30))
       visibilty_la.place(x=200,y=550)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',30))
       na.place(x=200,y=550)
      try:
       moon_la=Label(top,text=weather_info['moon_phase']['text'],bg='white',relief=RAISED,font=('bold',35))
       moon_la.place(x=1120,y=600)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',35))
       na.place(x=1200,y=600)
      try:
       pressure_la=Label(top,text=weather_info['barometer']['reading'],bg='white',relief=RAISED,font=('bold',35))
       pressure_la.place(x=1210,y=350)
      except KeyError:
       na = Label(top,text="NA",relief=RAISED,font=('bold',35))
       na.place(x=1210,y=350)

       #status bar containing units
      status_units=Label(top,text=weather_info['units'],bg='white',relief=SUNKEN,bd=1,height=1)
      status_units.pack(side=BOTTOM,fill=X)
      top.geometry('1366x700+-7+-2')
      top.wm_title("----------------------------ADVANCE WEATHER UPDATE---------------------- ")

      top.mainloop()