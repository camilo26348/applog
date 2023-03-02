from win32gui import GetForegroundWindow, GetWindowText
from time import sleep
from datetime import datetime
from socket import gethostname, gethostbyname
from os import environ as env
import requests

def get_visible_app():
    try:
        scr = GetForegroundWindow()
        value = GetWindowText(scr)
        if value:
            arr = value.split(' - ')
            app_name = arr[len(arr) - 1:len(arr)][0].__str__()
            app_title = ''
            if value.split(' - ' + app_name)[0].__str__():
                app_title = value.split(' - ' + app_name)[0].__str__()
            return app_name, app_title
    except Exception as e:
        return e.__str__()

if __name__ == '__main__':
    stop = False
    last_open_app = []
    first_time_open_app = ''
    last_open_app = get_visible_app()
    first_time_open_app = datetime.now()
    while not stop:
        try:
            time = datetime.now()
            user = env.get('USERNAME')
            pc = gethostname()
            ip = gethostbyname(pc)
            if not last_open_app == get_visible_app():
                #print(time.__str__(), pc, user, last_open_app[0], last_open_app[1], time-first_time_open_app)

                data = {
                    "date":time.__str__(),
                    "pc": pc,
                    "ip": ip,
                    "user": user,
                    "app_name": last_open_app[0],
                    "app_title": last_open_app[1],
                    "open_time": time - first_time_open_app
                }

                r = requests.post(url='http://10.176.1.234/pclog/api', data=data, timeout=2)

                last_open_app = get_visible_app()
                first_time_open_app = datetime.now()

                print(r.text, ' STATUS: ' + r.status_code.__str__())

            sleep(1)
        except Exception as e:
            sleep(2)
            print(e.__str__())
            pass