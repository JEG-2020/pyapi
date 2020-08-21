#!/usr/bin/python3

import requests
from datetime import datetime as dt

# define the URL we want to use
TIMEURL = "http://date.jsontest.com"
IPURL = "http://ip.jsontest.com"
POSTURL = "http://validate.jsontest.com/"

def main():
    # test data to validate as legal json
    # when a POST json= is replaced by the KEY "json"
    # the key "json" is mapped to a VALUE of the json to test
    # because the test item is a string, we can include whitespaces
    resp = requests.get(TIMEURL)
    mytime = resp.json()

    resp = requests.get(IPURL)
    myip = resp.json()
    print(mytime)
    print(myip)
    mysvr = open("/home/student/pyapi/jsontest/myservers.txt","r")

    mydata = {"json": "{'fruit': ['apple', 'pear'], 'vegetable': ['carrot']}" }

    # use requests library to send an HTTP POST
    resp = requests.post(POSTURL, data=mydata)

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjson = resp.json()

    # display our PYTHONIC data (LIST / DICT)
    print(respjson)

    # JUST display the value of "validate"
    print(f"Is your JSON valid? {respjson['validate']}")
    print(f"\nCurrent Time: {mytime['time']}")
    print(f"\nYour IP address is : {myip['ip']}")
    myjson = {}
    myjson["time"] = ({"time: {mytime["time"]}} , ip: {myip["ip"]}, mysvrs: {mysvr}\}\}') 
if __name__ == "__main__":
    main()


