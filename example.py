#! /usr/bin/env python3

from weather import API
import yaml
import unittest

with open("./config.yml", 'r') as ymlfile:
    cfg = yaml.safe_load(ymlfile)
api=API(cfg["API_KEY"])
    
current=api.current(zip_code="75094")

print("the current weather is %s with %s"%(
    current["weather"][0]["main"],current["weather"][0]["description"]
))

