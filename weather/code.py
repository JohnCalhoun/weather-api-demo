"""
This module implements an API for accessing weather data from OpenWeather
"""
import requests
from urllib.parse import urlencode

class API():
    """
        Main class for accessing OpenWeather API 
        # Arguments 
        api_key (str): API key for OpenWeather. 
        units (str): standard, metric, or imperial (default)
    """

    def __init__(self,api_key,units="imperial"):
        self.api_key=api_key
        self.units=units
        self.version="2.5"
        self.url_base="https://api.openweathermap.org/data/%s"%(self.version)

    def _params(self,zip_code,city_name,city_id,lat_lon,country_code):
        params={}
        if zip_code:
            params["zip"]='%s,%s'%(zip_code,country_code)
        elif city_name:
            params["q"]='%s,%s'%(city_name,country_code)
        elif city_id:
            params["id"]=city_id
        elif lat_lon:
            params["lat"]=lat_lon[0]
            params["lon"]=lat_lon[1]
        else:
            raise Exception('Must provide a location')
        return params
    
    def _request(self,path,params):
        _params=params.copy()
        _params["APPID"]=self.api_key
        _params["units"]=self.units
        
        url=self.url_base+"/"+path+"?"+urlencode(_params)
        r=requests.get(url)
        data=r.json()
        if str(data.get("cod",None))!='200':
            raise Exception(data.get("message",data.get("cod")))
        return data
       
    def request(self,path,params):
        """
        # Arguments
        path (str): the path in the api to send to eg. weather or forecast
        params (dict): additional params to be sent of url params in the request
        """
        return self._request(path,params)

    def current(self,zip_code=None,city_name=None,city_id=None,lat_lon=None,country_code="us"):
        params=self._params(zip_code,city_name,city_id,lat_lon,country_code)
        return self._request("weather",params)

    def forecast(self,zip_code=None,city_name=None,city_id=None,lat_lon=None,country_code="us"):
        params=self._params(zip_code,city_name,city_id,lat_lon,country_code)
        return self._request("forecast",params)["list"]
