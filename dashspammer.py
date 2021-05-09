from threading import Timer
import time
from tkinter.constants import COMMAND, END, FALSE
import urllib.request as urllib2
import tkinter as tk
from tkinter import ttk
import time as t
from tkinter import messagebox
import googlesearch
import webbrowser
from bs4 import BeautifulSoup
import re
from urllib.request import url2pathname
from urllib.request import url2pathname
import urllib
import urllib3
import pyautogui
import requests











 

window = tk.Tk()

buttonClicked = False


window.title("dash-spammer") 
window.minsize(600,400) 


 
def gui(buttonClicked):


 
 
 if(buttonClicked == True):
  result = name.get()
  result1 = name1.get()
  result2 = name2.get()
 
  
  for i in range(0, result1):
       pyautogui.write(result)
       pyautogui.press("enter")
       time.sleep(result2)


   

       


 
 
 


button = ttk.Button(window, text = "Enter", command= gui(buttonClicked))
             
button.grid(column= 15, row = 1) 


name = tk.StringVar()
nameEntered = ttk.Entry(window, width = 15, textvariable = name)
nameEntered.grid(column = 10, row = 1) 




label = ttk.Label(window, text = "text") # text
label.grid(column = 0, row = 1) 



 


button1 = ttk.Button(window, text = "Enter", command=gui(buttonClicked))
             
button1.grid(column= 15, row = 2) 







label = ttk.Label(window, text = "times") # text
label.grid(column = 0, row = 2) 


name1 = tk.IntVar()
nameEntered1 = ttk.Entry(window, width = 15, textvariable = name1)
nameEntered1.grid(column = 10, row = 2) 


 


button1 = ttk.Button(window, text = "Enter", command = print("good"))
             
button1.grid(column= 15, row = 3) 




name2 = tk.IntVar()

nameEntered2 = ttk.Entry(window, width = 15, textvariable = name2)
nameEntered2.grid(column = 10, row = 3) 



label = ttk.Label(window, text = "quick") 
label.grid(column = 0, row = 3) 





button3 = ttk.Button(window, text = "start", command=lambda buttonClicked = True:gui(buttonClicked))
             
button3.grid(column= 10, row = 5) 







window.mainloop()
