#! /usr/bin/env python3

from weather import API
import yaml
import unittest

class WeatherMethods(unittest.TestCase):
    def setUp(self):
        with open("./config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        self.api=API(cfg["API_KEY"])
    
    def test_current(self):
        current=self.api.current(zip_code="75094")

    def test_forecast(self):
        forecast=self.api.forecast(zip_code="75094")
    
    def test_city_name(self):
        forecast=self.api.forecast(city_name="London",country_code="uk")

    def test_city_id(self):
        forecast=self.api.forecast(city_id="524901")

    def test_lat_lon(self):
        forecast=self.api.forecast(lat_lon=["35","139"])

