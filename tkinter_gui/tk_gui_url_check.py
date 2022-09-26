import requests
import datetime
from tkinter import *


app = Tk()
app.geometry("700x300")
app.title('Tools Checker')


def time_now():
    now = datetime.datetime.now()
    t_now = now.strftime('%H:%M:%S %d-%m-%Y')
    return t_now


def check():
    global interval
    # table labels
    table_label = Label(app, text='Tool', fg='blue', font='calibri 12 bold').grid(row=1, column=1)
    status_label = Label(app, text='Status', fg='blue', font='calibri 12 bold').grid(row=1, column=2)
    log_label = Label(app, text='          Log          ', fg='blue', font='calibri 12 bold').grid(row=1, column=3)
    check_label = Label(app, text='Check in:', fg='blue', font='calibri 12 bold').grid(row=1, column=4)
    i = 2
    j = 2
    try:
        urls_file = open('urls-config', 'r')
        urls_data = urls_file.read()
        urls = urls_data.split('\n')
        urls_file.close()
    except:
        pass

    try:
        conf_len = len(urls)
        for t in range(conf_len - (conf_len - 1)):
            interval = int(urls[t])
        for url in range(len(urls)):
            url = urls[url]
            list_url = url.split(' ')
            try:
                e = Entry(app, width=20, fg='blue')
                e.grid(row=i, column=1, sticky=E)
                e.insert(END, list_url[1])
                i = i + 1
                response = requests.get(list_url[2]) #for use certificate -> verify=/path/to/crt/file
                status = str(response.status_code)
                if status == '200':
                    s = Entry(app, width=8, fg='white', bg='green', justify='center')
                    s.grid(row=j, column=2, sticky=E)
                    s.insert(END, status)
                    j = j + 1
                else:
                    s = Entry(app, width=8, fg='white', bg='red', justify='center')
                    s.grid(row=j, column=2, sticky=E)
                    s.insert(END, status)
                    log = Entry(app, width=25, fg='blue')
                    log.grid(row=j, column=3, sticky=E)
                    log.insert(END, list_url[1] + ' ' + time_now())
                    j = j + 1
            except IndexError:
                pass
            except:
                s = Entry(app, width=8, fg='white', bg='red', justify='center')
                s.grid(row=j, column=2, sticky=E)
                s.insert(END, 'Error')
                log = Entry(app, width=25, fg='blue')
                log.grid(row=j, column=3, sticky=E)
                log.insert(END, list_url[1] + ' ' + time_now())
                j = j + 1
    except NameError:
        pass
    clock = Entry(app, width=22, fg='blue', justify='center')
    clock.grid(row=1, column=5, sticky=E)
    clock.insert(END, time_now())
    app.after(interval, check)


app.after(100,check)
app.mainloop()
