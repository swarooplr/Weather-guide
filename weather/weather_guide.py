from tkinter import *
from functools import partial
import tkinter.messagebox
import pywapi
import weather.basic_weather_update
import weather.advanced_weather_update
import weather.compare
import weather.forecast
import weather.sports_index
import weather.outdoor_index
import weather.living_index

    #pop window control unit
def info_generator2(choice,b_type):
    global r

    if(b_type==1):
        weather.basic_weather_update.basic_weather_update_window2(pywapi.get_weather_from_weather_com(choice[r.get()]))
    elif(b_type==2):
        weather.advanced_weather_update.advanced_weather_update_window2(pywapi.get_weather_from_weather_com(choice[r.get()]))
    elif(b_type==3):
        weather.forecast.forecast2(pywapi.get_weather_from_weather_com(choice[r.get()]))
    elif(b_type==4):
        weather.outdoor_index.out2(pywapi.get_weather_from_weather_com(choice[r.get()]))
    elif(b_type==5):
        weather.sports_index.out2(pywapi.get_weather_from_weather_com(choice[r.get()]))
    elif(b_type==6):
        weather.living_index.out2(pywapi.get_weather_from_weather_com(choice[r.get()]))
    else:
        pass



def button_screen2_window(c,root):




    global r
    f=Frame(root).place(x=0,y=0,relwidth=1,relheight=1)


    background=PhotoImage(file='wallpaper.png')
    label2=Label(f,image=background,relief=SUNKEN)
    label2.place(x=0,y=0,relwidth=1,relheight=1)

    choice={}
    j=0
    r.set(0)
    for i in c:
        choice[j]=i
        Radiobutton(f,text=c[i],font='bold',variable=r,value=j).place(x=20,y=100+j*50)
        j=j+1


    bw=Button(f,text='Basic weather update',font='bold',relief=RAISED,command=partial(info_generator2,choice,1)).place(x=900,y=200)
    aw=Button(f,text='Advanced weather update',font='bold',relief=RAISED,command=partial(info_generator2,choice,2)).place(x=900,y=250)
    fr=Button(f,text='Forecast',font='bold',relief=RAISED,command=partial(info_generator2,choice,3)).place(x=900,y=300)
    oi=Button(f,text='Outdoor index',font='bold',relief=RAISED,command=partial(info_generator2,choice,4)).place(x=900,y=350)
    si=Button(f,text='Sports index',font='bold',relief=RAISED,command=partial(info_generator2,choice,5)).place(x=900,y=400)
    li=Button(f,text='Living index',font='bold',relief=RAISED,command=partial(info_generator2,choice,6)).place(x=900,y=450)

    Change_button=Button(f,text="Change theme",font='bold',width=35,height=1,command=partial(options_screen,c))
    Change_button.place(x=1000,y=20)

    quit=Button(f,text='BACK',font='bold',command = main_screen).place(x=0,y=10)


    root.mainloop()





def info_generator(city_id,x):
#1366*768    455.33*384   341*256
    global update_mode_switch
    global forecast_switch
    global outdoor_index_switch
    global sports_index_switch




    weather_info= pywapi.get_weather_from_weather_com(city_id)                           #getting weather


    if(update_mode_switch.get()==1):


        weather.basic_weather_update.basic_weather_update_window(weather_info,forecast_switch.get(),outdoor_index_switch.get(),sports_index_switch.get(),living_index_switch.get())

    else:

        weather.advanced_weather_update.advanced_weather_update_window(weather_info,forecast_switch.get(),outdoor_index_switch.get(),sports_index_switch.get(),living_index_switch.get())








def options_screen(city_ids):
        button_screen=Frame(root,relief=SUNKEN)
        button_screen.place(x=0,y=0,relwidth=1,relheight=1)



        background=PhotoImage(file='wallpaper.png')
        label2=Label(button_screen,image=background,relief=SUNKEN)
        label2.place(x=0,y=0,relwidth=1,relheight=1)

        #check buttons

        global update_mode_switchs
        global forecast_switch
        global outdoor_index_switch
        global sports_index_switch

        update_mode_switch.set(1)
        forecast_switch.set(0)
        outdoor_index_switch.set(0)
        sports_index_switch.set(0)
        living_index_switch.set(0)

        bw=Radiobutton(button_screen,text='Basic weather update',font='bold',relief=SUNKEN,variable = update_mode_switch ,value = 1).place(x=900,y=100)
        aw=Radiobutton(button_screen,text='Advanced weather update',font='bold',relief=SUNKEN,variable = update_mode_switch,value = 2).place(x=900,y=150)
        fr=Checkbutton(button_screen,text='Forecast',font='bold',relief=SUNKEN,variable= forecast_switch).place(x=900,y=300)
        oi=Checkbutton(button_screen,text='Outdoor index',font='bold',relief=SUNKEN,variable=outdoor_index_switch ).place(x=900,y=350)
        si=Checkbutton(button_screen,text='Sports index',font='bold',relief=SUNKEN,variable=sports_index_switch).place(x=900,y=400)
        li=Checkbutton(button_screen,text='Living index',font='bold',relief=SUNKEN,variable=living_index_switch).place(x=900,y=450)
        #city option buttons

        quit=Button(button_screen,text='BACK',font='bold',command = main_screen).place(x=0,y=10)


        choice={}                                                                           #an empty dictinary
        count=1
        for i in city_ids:                                                                  #for every key in loaction id dictionary
            choice[count] = i
            count+=1
        for count in  choice:
             b=Button(button_screen,text=city_ids[choice[count]],fg='black',font='20',bg='white',width=35,height=1,command=partial(info_generator,choice[count],update_mode_switch))         #creation of buttons
             b.place(x=20,y=100+count*50)


        Change_button=Button(button_screen,text="Change theme",font='bold',width=35,height=1,command=partial(button_screen2_window,city_ids,root))
        Change_button.place(x=1000,y=20)
        root.mainloop()




def city_location_id_search(city_name):

    location_ids_of_cities = pywapi.get_location_ids(city_name.get())                #getting location ids from the given entery

    if(len(location_ids_of_cities)==0):
      tkinter.messagebox.showinfo('invalid','City not found')

    else:
      options_screen(location_ids_of_cities)                                           #calling the option_screen function to create new window

def main_screen():




    search_frame=Frame(root,relief=SUNKEN)                               #search frame
    search_frame.place(x=0,y=0,relwidth=1,relheight=1)



    back_ground_image=PhotoImage(file='background.png')
    label1=Label(search_frame,image=back_ground_image,relief=SUNKEN)     #search frame wallpaper
    label1.place(x=0,y=0,relwidth=1,relheight=1)

    button_compare = Button(search_frame,relief=SUNKEN,bd=4,width=20,height=3,fg='black',bg='white',font='30',text='COMPARE',command=partial(weather.compare.compare,root))
    button_compare.place(x=720,y=350)

    entry_text = StringVar()                                             #creating a entery box and variable to accept values
    entry_text.set("enter here")
    search_column=Entry(search_frame,relief=SUNKEN,bd=6,width=30,fg='black',font='bold',textvariable=entry_text)
    search_column.place(x=650,y=250)

    go_button=Button(search_frame,text='GO',fg='black',bg='white',width=10,height=1,relief=RAISED,command=partial(city_location_id_search,entry_text))
    go_button.place(x=930,y=250)                                         #creating a go button to get loaction options





    root.mainloop()



#STARTERS


root = Tk()                                                              #main_window
root.geometry('1366x700+-7+-2')
root.wm_title("-----------------------------------WEATHER GUIDE----------------------------------------- ")
wallpaper_indicator = "default"

forecast_switch = IntVar()
update_mode_switch=IntVar()
outdoor_index_switch=IntVar()
sports_index_switch=IntVar()
living_index_switch=IntVar()
r = IntVar()

main_screen()
