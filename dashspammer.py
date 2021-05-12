import datetime
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
import sys
import os
from tkinter import Tk, Label, Button




print("▄▀▀█▄▄   ▄▀▀█▄   ▄▀▀▀▀▄  ▄▀▀▄ ▄▄")
print('█ ▄▀   █ ▐ ▄▀ ▀▄ █ █   ▐ █  █   ▄▀ ')
print("▐ █    █   █▄▄▄█    ▀▄   ▐  █▄▄▄█  ")
print("  █    █  ▄▀   █ ▀▄   █     █   █  ")
print(" ▄▀▄▄▄▄▀ █   ▄▀   █▀▀▀     ▄▀  ▄▀  ")


print("_________________________________________________")


window = tk.Tk()

buttonClicked = False
everyone = False
counting = False
graffiti = False
f = open('Graffiti.txt', 'r+')

window.title("love-spammer") 
window.minsize(600,400) 
date = datetime.datetime.today()
def restart_program():
      
    python = sys.executable
    os.execl(python, python, * sys.argv)
button = ttk.Button(window, text="Quit", command=restart_program)
button.grid(column=10, row=12)
 
def gui(buttonClicked, everyone, counting, graffiti):

 if(graffiti == True):
  reading = int(input("how many lines is your graffiti(enter 0 if you have no graffiti): "))


  for i in range(0, reading):

      x = str(f.readline())
      time.sleep(2)

     
      pyautogui.write(x)
      time.sleep(1)
      pyautogui.press("enter")
      
      
    

 if (counting == True):
    
     result1 = name1.get()
     result2 = name2.get()
     print(date)
     print("Sending Attack")
     for i in range(0, result1):
         string = str(i)
         pyautogui.write(string)
         pyautogui.press("enter")
         time.sleep(result2)
         

   

 
 if(everyone == True):
  result = name.get()
  result1 = name1.get()
  result2 = name2.get()
  print(date)
  print("Sending Attack" )
  

 
  
  for i in range(0, result1):
       pyautogui.write(result)
       pyautogui.press("enter")
       pyautogui.press("enter")
       time.sleep(result2)
 if(buttonClicked == True):
      result = name.get()
      result1 = name1.get()
      result2 = name2.get()
      print(date)
      print("Sending Attack" )
    

  
      for i in range(0, result1):
       pyautogui.write(result)
      
       pyautogui.press("enter")
       time.sleep(result2)


 


   

       


 
 
 


button = ttk.Button(window, text = "Enter", command= gui(buttonClicked, everyone, counting, graffiti))
             
button.grid(column= 15, row = 1) 


name = tk.StringVar()
nameEntered = ttk.Entry(window, width = 15, textvariable = name)
nameEntered.grid(column = 10, row = 1) 




label = ttk.Label(window, text = "Text") 
label.grid(column = 0, row = 1) 



 


button1 = ttk.Button(window, text = "Enter", command=gui(buttonClicked, everyone , counting, graffiti))
             
button1.grid(column= 15, row = 2) 










label = ttk.Label(window, text = "Times") # text
label.grid(column = 0, row = 2) 


name1 = tk.IntVar()
nameEntered1 = ttk.Entry(window, width = 15, textvariable = name1)
nameEntered1.grid(column = 10, row = 2) 


 


button1 = ttk.Button(window, text = "Enter", command = gui(buttonClicked, everyone, counting, graffiti))
             
button1.grid(column= 15, row = 3) 




name2 = tk.IntVar()

nameEntered2 = ttk.Entry(window, width = 15, textvariable = name2)
nameEntered2.grid(column = 10, row = 3) 



label = ttk.Label(window, text = "Quick") 
label.grid(column = 0, row = 3) 





button3 = ttk.Button(window, text = "Normal Spam", command=lambda buttonClicked = True:gui(buttonClicked, everyone, counting, graffiti))
             
button3.grid(column= 10, row = 4) 





button1 = ttk.Button(window, text = "Discord Spam", command=lambda everyone = True:gui(buttonClicked, everyone, counting, graffiti))
             
button1.grid(column= 10, row = 5) 



button1 = ttk.Button(window, text = "Counting", command=lambda counting = True:gui(buttonClicked, everyone, counting, graffiti))
             
button1.grid(column= 10, row = 6) 

button1 = ttk.Button(window, text = "Graffiti", command=lambda graffiti = True:gui(buttonClicked, everyone, counting, graffiti))
             
button1.grid(column= 10, row = 8) 







window.mainloop()
