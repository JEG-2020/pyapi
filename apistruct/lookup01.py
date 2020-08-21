#!/usr/bin/env python3
import requests

def main():
  mytoken = 'fb5ba470ffdbfb3bbe5e7cc731b57c944ff15d8889483b74'
  myapi = "https://fonoapi.freshpixl.com/v1/getlatest"
  mybuiltapi = myapi + "?token=" + mytoken
  
  ## translate our JSON response to a series of Python lists and dictionaries
  myjson = requests.get(mybuiltapi).json()
  
  ## Display a list of what inside our JSON
  for x in myjson:
    print(x)
  
if __name__ == '__main__':
    main()
