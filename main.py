# coding=utf-8

import requests
import dateutil.parser
import datetime
import os
def print_hi(name):
    r = requests.get("https://api-v3.mbta.com/predictions?filter%5Bstop%5D=70066")
    print r.json()["data"][0]["attributes"]["arrival_time"]
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.
    yourdate = dateutil.parser.parse(r.json()["data"][0]["attributes"]["arrival_time"])
    print(yourdate)
    print(datetime.datetime.now())
    date = str(yourdate.replace(tzinfo=None)-datetime.datetime.now().replace(tzinfo=None))
    os.system('sudo ../rpi-rgb-led-matrix/examples-api-use/scrolling-text-example -f "../rpi-rgb-led-matrix/fonts/7x13.bdf" --led-rows=32 --led-cols=64 --led-slowdown-gpio=3 -x 32 -y 9  -C 32,24,204 -B 255,247,3 "' + date + '"')
#subtract the current time from the arrival time

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# [1, 2, 3]