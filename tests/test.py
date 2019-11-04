#! /usr/bin/env python3

from weather import API
import yaml
import unittest

class WeatherMethods(unittest.TestCase):
    def setUp(self):
        with open("./config.yml", 'r') as ymlfile:
            cfg = yaml.safe_load(ymlfile)
        self.api=API(cfg["API_KEY"])
    
    def test_current(self):
        result=self.api.current(zip_code="75094")

    def test_forecast(self):
        result=self.api.forecast(zip_code="75094")
    
    def test_city_name(self):
        result=self.api.forecast(city_name="London",country_code="uk")

    def test_city_id(self):
        result=self.api.forecast(city_id="524901")

    def test_lat_lon(self):
        result=self.api.forecast(lat_lon=["35","139"])
    
    def test_request(self):
        result=self.api.request("weather",{"zip":"75094,us"})
        
