#! /usr/bin/env python3

from weather import API
import yaml
import unittest
import time
import argparse

parser = argparse.ArgumentParser("example.py")
parser.add_argument("zip_code", 
    help="the zip code of where you want the weather", type=str)
args = parser.parse_args()
zip_code=args.zip_code

with open("./config.yml", 'r') as ymlfile:
    cfg = yaml.safe_load(ymlfile)

api=API(cfg["API_KEY"])

current=api.current(zip_code=zip_code)
forecast=api.forecast(zip_code=zip_code)

print("the current weather for %s is %s with %s"%(
    zip_code,
    current["weather"][0]["main"],
    current["weather"][0]["description"]
))

def info(data):
    t=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data["dt"]))
    temp=data["main"]["temp"]
    return "%s: temp=%s"%(t,temp)

print("")
print("Forecast")
for x in forecast[:4]:
    print(info(x))
