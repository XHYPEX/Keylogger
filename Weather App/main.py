from tkinter import *
import requests



#6c3708199e561ddfbe9319cd000d2c2a
#api.openweathermap.org/data/2.5/forecast?q={city name}&appid={API key}

def display():
    city_label = Label(root, text=weather['name'], font='Montseratt')
    city_label.grid(row=0, sticky=W)
    weather_label = Label(root, text=weather['weather'][0]['description'], font='Montseratt')
    weather_label.grid(row=1, sticky=W)
    temp_label = Label(root, text=str(weather['main']['temp']) + " C", font='Futura 20 bold')
    temp_label.grid(row=2, sticky=W)

def connect():
    try:
        global weather
        weather_key = '6c3708199e561ddfbe9319cd000d2c2a'
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'appid': weather_key, 'q': 'Balikpapan', 'units': 'metric'}
        response = requests.get(url, params=params)
        weather = response.json()
        display()
    except Exception as e:
        print(e.args)

root = Tk()
root.title('Weather App')

# get screen width and height
ws = root.winfo_screenwidth()
sh = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (400, 150, 1136, 0))
connect()
reconnect = Button(text="Reconnect", bg="black", fg="white", command=connect)
reconnect.grid(row=3, padx=20, pady=(20,10))



root.mainloop()