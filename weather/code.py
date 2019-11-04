"""
This module implements an API for accessing weather data from OpenWeather
"""
import requests
from urllib.parse import urlencode

class API():
    """
        Main class for accessing OpenWeather API 
        
        ```python
            from weather import API
            import yaml

            zip_code="75094"

            # Load API from a config file because DONT PUT IN CODE!
            with open("./config.yml", 'r') as ymlfile:
                cfg = yaml.safe_load(ymlfile)

            api=API(cfg["API_KEY"])

            current=api.current(zip_code=zip_code)
        ```
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
       
        # Returns
        The raw JSON results returned as a nested dict object.
        """
        return self._request(path,params)

    def current(self,zip_code=None,city_name=None,city_id=None,lat_lon=None,country_code="us"):
        """
        get the current weather for a location. Must specifiy one of the following combinations:
        - zip_code and country_code
        - city_name and country_code
        - city_id
        - lat_lon

        # Arguments
        zip_code (str): zip code of location
        city_name (str): name of the City such as 'London'
        city_id (str): OpenWeather city ID
        lat_lon (array of str): the first item is the latatude and the second is the longitude
        country_code (str): example 'us' or 'uk'
	
        # Returns
        ```json
            {
              "coord": {
                "lon": -122.08,
                "lat": 37.39
              },
              "weather": [
                {
                  "id": 800,
                  "main": "Clear",
                  "description": "clear sky",
                  "icon": "01d"
                }
              ],
              "base": "stations",
              "main": {
                "temp": 296.71,
                "pressure": 1013,
                "humidity": 53,
                "temp_min": 294.82,
                "temp_max": 298.71
              },
              "visibility": 16093,
              "wind": {
                "speed": 1.5,
                "deg": 350
              },
              "clouds": {
                "all": 1
              },
              "dt": 1560350645,
              "sys": {
                "type": 1,
                "id": 5122,
                "message": 0.0139,
                "country": "US",
                "sunrise": 1560343627,
                "sunset": 1560396563
              },
              "timezone": -25200,
              "id": 420006353,
              "name": "Mountain View",
              "cod": 200
            }
        ```
        """
        params=self._params(zip_code,city_name,city_id,lat_lon,country_code)
        return self._request("weather",params)

    def forecast(self,zip_code=None,city_name=None,city_id=None,lat_lon=None,country_code="us"):
        """
        get the 5 day, 3 hour forecast a location. Must specifiy one of the following combinations:
        - zip_code and country_code
        - city_name and country_code
        - city_id
        - lat_lon

        # Arguments
        zip_code (str): zip code of location
        city_name (str): name of the City such as 'London'
        city_id (str): OpenWeather city ID
        lat_lon (array of str): the first item is the latatude and the second is the longitude
        country_code (str): example 'us' or 'uk'

        # Returns
        ```json
			[{
                "dt":1406106000,
                "main":{
                    "temp":298.77,
                    "temp_min":298.77,
                    "temp_max":298.774,
                    "pressure":1005.93,
                    "sea_level":1018.18,
                    "grnd_level":1005.93,
                    "humidity":87,
                    "temp_kf":0.26},
                "weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],
                "clouds":{"all":88},
                "wind":{"speed":5.71,"deg":229.501},
                "sys":{"pod":"d"},
                "dt_txt":"2014-07-23 09:00:00"
            }]
        ```
        """

        params=self._params(zip_code,city_name,city_id,lat_lon,country_code)
        return self._request("forecast",params)["list"]
