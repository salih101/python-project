import PySimpleGUI as sg
import requests
from bs4 import BeautifulSoup

sg.theme('DarkGrey14')  
url ='https://weather.com/en-IN/weather/today/l/aedafa26444d6995ab6ac961b7d22514fbe8042afc9b8ab568eef77aab1f1e3b'

layout =[  [sg.Push(),sg.Text('Weather App',font="_14"),sg.Push()],
            [sg.Text('',key="location")],
            [sg.Push(),sg.Text('Temperature(°C):'),sg.Text('',key="weather",font="_14"),sg.Push()],
            [sg.Push(),sg.Button('Update'),sg.Button('Exit'),sg.Push()]
        ]
    
window = sg.Window('Weather App', layout)
while True:
    event,values= window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': 
        break
    if event == 'Update':
        data = requests.get(url)
        weather_data = BeautifulSoup(data.text,'html.parser')
        curr_weather = weather_data.find("span",class_ = "CurrentConditions--tempValue--MHmYY")
        curr_location = weather_data.find("div",class_ = "CurrentConditions--header--kbXKR")
        window['location'].update(curr_location.get_text())
        window['weather'].update(curr_weather.get_text())
window.close()
