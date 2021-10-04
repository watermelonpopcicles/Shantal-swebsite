#import the library
import tkinter as tk
import time
import requests
import json
import datetime
import tkinter as tk

info2 = ""
#city = input("What city are you in?")
def getcity():
    global info2
    city = town.get()
    url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=8fe79b85155beefc0a3882d4b1377ddd&units=imperial"
    x = requests.get(url)
    repeat = True
    #info=(x.content)
    #info2=json.loads(info)
    #print(info2["main"])

    info=(x.content)
    info2=json.loads(info)
#print(info2)
    infodc6.pack_forget()
    q.pack_forget()
    w.pack_forget()
    info91.pack()
    a.pack()
    o.pack()
    e.pack()

   


def getinfo():
    userChoice = selection.get()
    
    
    if (userChoice == "1"):
        place = info2["coord"]
        longitude = place["lon"]
        latitude = place["lat"]
        printout = ("The longitude is: " + str(longitude) + "\n" +
                      "The latitude is: " + str(latitude))
        e.config(text = printout )

    if (userChoice == "2"):
        temp = info2["main"]
        degrees = temp["temp"]
        feelsLike = temp["feels_like"]
        minimal = temp["temp_min"]
        maximum = temp["temp_max"]
        humidity = temp["humidity"]
        pressure = temp["pressure"]
        
        togo2 = ("Today's temperature is: " + str(degrees) + " degrees F" + "\n"
                + "It feel's like: " + str(feelsLike) + " degrees F" "\n" +
                "The minimum temperature and the maximum temperature today are: " + str(minimal) + " and " + str(maximum) + " degrees F" + "\n" +
                "The humdity today is: " + str(humidity) + " lbs per feet cubed" + "\n" +
                "The pressure today is: " + str(pressure) + " PSI")
        e.config(text = togo2 )

    if (userChoice == "3"):
        sunrise = int(info2["sys"]["sunrise"])+ int(info2["timezone"])
        sunrise = time.strftime("%H:%M:%S",time.gmtime(sunrise))
        sdt = datetime.datetime.strptime(sunrise,"%H:%M:%S").time()

        sunset = int(info2["sys"]["sunset"])+ int(info2["timezone"])
        sunset = time.strftime("%H:%M:%S",time.gmtime(sunset))
        setdt = datetime.datetime.strptime(sunset,"%H:%M:%S").time()

        togo = str(sdt)+"\n"+str(setdt)
        e.config(text = togo)
        

    if (userChoice == "4"):
        e.config(text = info2["timezone"])
        

    #replay = input("Do you want more information about a city? yes or no")


    
top = tk.Tk()
top.configure(bg = "light yellow")
town = tk.StringVar()
selection = tk.StringVar()

#label
infodc6 = tk.Label(top,text = """

      Hello Well come my Weather forcast app, where are you? 





                """)
infodc6.configure(bg = "light yellow")
infodc6.pack()

#entry
q = tk.Entry (top,textvariable = town)
q.pack()

#button
w = tk.Button (top,command = getcity, text = " Enter ", width=17,height=5, bg = "light blue",)
w.pack()


#label
info91 = tk.Label(top,text = 
    """Info:
        1. Coordinates
        2. Weather
        3. Sunrise/Sunset
        4. Timezone
        Choose a number. What information do you want?
        Put a different number if you want to know something else. """)
info91.configure(bg = "light yellow")
#entry
a = tk.Entry (top,textvariable = selection)

#button
o = tk.Button (top,command = getinfo, text = " Enter ", width=17,height=5, bg = "light blue",)

#entry
a = tk.Entry (top,textvariable = selection)

#label
e = tk.Label(top,text = "")


                
top.mainloop()


#Print the info

#info=(x.content)
#info2=json.loads(info)
#print(info2["weather"])




