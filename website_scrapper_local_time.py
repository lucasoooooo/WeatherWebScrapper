#By Lucas Balangero, 7/8/2019
# Will eventually be alarm clock with weather display,

# Currently has: "degrees for the week", "time"
# Missing: "Alarm", "Button implentation", "rasberry pi implementation"
# Currently working on: N/A

import requests, time
from bs4 import BeautifulSoup
from tkinter import *

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

class MainFunc:
    def __init__ (self):
        self.hourX=12
        self.lblTime = Label(window, text=self.hourX, font =("Arial Bold",40))
        self.lblTemp1 = Label(window, text = -1, font=("Arial Bold", 25))
        self.lblTemp2 = Label(window, text = -1, font=("Arial Bold", 25))
        self.lbl1 = Label(window,text = "Right Now   Today   Tonight", font=("Arial Bold",25))
        self.lbl2 = Label(window,text = "Tomorrow   T-Night   Fornite", font=("Arial Bold",25))
        self.lblTime.pack()
        self.lbl1.pack()
        self.lblTemp1.pack()
        self.lbl2.pack()
        self.lblTemp2.pack()

        self.update_label()
        
    def update_label (self):

        if self.hourX == 12:
            #weather channel website
            URL_temp = 'https://weather.com/weather/today/l/94f449f57d52cb8a88cfb563e644e16eeb50b9d3f653ce01485d7fa6a1d764b6'
            page_temp  = requests.get(URL_temp, headers = headers)
            soup = BeautifulSoup(page_temp.content, 'html.parser')
            self.temps= []
            self.temps.append(int(soup.find("div", {"class": "today_nowcard-temp"}).get_text()[0:2]))
            for div in soup.find_all ("div", {"class": "today-daypart-temp"}):
                self.temps.append(int(div.get_text()[0:2]))
            self.lblTemp1['text']=('%d\xb0F\t%d\xb0F\t%d\xb0F' %(self.temps[0],self.temps[1],self.temps[2]))
            self.lblTemp2['text']=('%d\xb0F\t%d\xb0F\t%d\xb0F' %(self.temps[3],self.temps[4],self.temps[5]))
        timeX= time.asctime()
        self.hourX = timeX[11:13]
        self.lblTime['text']= (timeX[0:19])
        self.lblTime.after(10, self.update_label)

window = Tk()
window.title("Lucas Alarm Clock")
MainFunc()
window.mainloop()