#!/usr/bin/python3
import time
import datetime as dt

bday= dt.datetime(1970,11,10)
now = dt.datetime.now()
print(bday)
mdiff = now -bday
print(f"{mdiff.total_seconds()} seconds since Birthdate:{bday}")
def main():
    rightmeow = time.strftime("%Y-%m-%d")
    with open(rightmeow + '-example.txt', 'w') as f:
        f.write('File with current date created!\n')

    hourtime = time.strftime("%H")
    with open(hourtime + '-example.txt', 'w') as f:
        f.write('File with hour timestamp created!\n')
  
    yearmonth = time.strftime("%Y-%B")
    with open(yearmonth + '-reporting.txt', 'w') as f:
        f.write('File with monthly timestamp created!\n')

if __name__ == '__main__':
    main()

