# coding=utf-8

import requests
import dateutil.parser
import datetime
def print_hi(name):
    r = requests.get("https://api-v3.mbta.com/predictions?filter%5Bstop%5D=70066")
    print r.json()["data"][0]["attributes"]["arrival_time"]
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.
    yourdate = dateutil.parser.parse(r.json()["data"][0]["attributes"]["arrival_time"])
    print(yourdate)
    print(datetime.datetime.now())
    print(yourdate.replace(tzinfo=None)-datetime.datetime.now().replace(tzinfo=None))
#subtract the current time from the arrival time

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# [1, 2, 3]
