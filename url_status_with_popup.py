import webbrowser
import requests
from win10toast_click import ToastNotifier
import time
from os import system, name


def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def open_web():
    try:
        webbrowser.open(list_url[1])
    finally:
        print('Failed to open ' + list_url[1])


while 1:
    urls_file = open('config', 'r')
    data = urls_file.read()
    urls = data.split('\n')
    urls_file.close()
    toast = ToastNotifier()
    for url in urls:
        list_url = url.split(' ')
        print(list_url[0])
        try:
            response = requests.get(list_url[1]) #for use certificate -> verify = /path/to/crt/file
            status = str(response.status_code)
            if status == '200':
                print(status)
            else:
                print('Error ' + status)
                toast.show_toast('Error', list_url[0] + ' not working Code status: ' + status, duration=10, callback_on_click=open_web)
        except:
            toast.show_toast('Error', list_url[0] + ' not working ', duration=10, callback_on_click=open_web)
            print('Error')
    clear_screen()
    time.sleep(5)
            
