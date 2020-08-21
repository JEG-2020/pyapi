#!/usr/bin/env python3
import requests
import argparse

def main():
  mytoken = 'fb5ba470ffdbfb3bbe5e7cc731b57c944ff15d8889483b74'
  myapi = "https://fonoapi.freshpixl.com/v1/getlatest"
  mybuiltapi = myapi + "?token=" + mytoken
  
  parser = argparse.ArgumentParser("Send BrandName")
  parser.add_argument("brand",help="which brand ?")
  args = parser.parse_args()

  ## ask user for a brand to search on
  #brand = input("What brand of device are you searching for?")
  #brand = "&brand=" + brand
  brand = "&brand=" + args.brand
  ## translate our JSON response to a series of Python lists and dictionaries
  myjson = requests.get(mybuiltapi + brand).json()
  #mydict = dict(myjson) 
  #print(type(mydict))
  
  #(myjson.index()))

  ## Display a list of what inside our JSON
  for x in myjson:
    print(x)
  
if __name__ == '__main__':
  main()

