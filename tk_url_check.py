import requests
import time
from os import system, name
import tkinter as tk
from tkinter import messagebox


def info(message, title="Error!"):
    root = tk.Tk()
    root.overrideredirect(1)
    root.withdraw()
    messagebox.showerror(title, message)
    root.destroy()


#info("Messagebox is cool")

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


while 1:
    urls_file = open('config', 'r')
    data = urls_file.read()
    urls = data.split('\n')
    urls_file.close()
    for url in urls:
        list_url = url.split(' ')
        try:
            response = requests.get(list_url[1]) #for use certificate -> verify=/path/to/crt/file
            status = str(response.status_code)
            if status == '200':
                print(list_url[0] + ' ' + status)
            else:
                print('Error ' + list_url[0] + ' ' + status)
                info(list_url[0] + ' not working Code status: ' + status)
        except:
            info(list_url[0] + ' not working ')
            print('Error ' + list_url[0])
    time.sleep(5)
    clear_screen()
