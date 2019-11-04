<h1 id="weather">weather</h1>


<h2 id="weather.API">API</h2>

```python
API(self, api_key, units='imperial')
```

Main class for accessing OpenWeather API

__Arguments__

- __api_key (str)__: API key for OpenWeather.
- __units (str)__: standard, metric, or imperial (default)

<h3 id="weather.API.request">request</h3>

```python
API.request(self, path, params)
```

__Arguments__

- __path (str)__: the path in the api to send to eg. weather or forecast
- __params (dict)__: additional params to be sent of url params in the request

<h3 id="weather.API.current">current</h3>

```python
API.current(self, zip_code=None, city_name=None, city_id=None, lat_lon=None, country_code='us')
```

get the current weather for a location. Must specifiy one of the following combinations:
- zip_code and country_code
- city_name and country_code
- city_id
- lat_lon

__Arguments__

- __zip_code (str)__: zip code of location
- __city_name (str)__: name of the City such as 'London'
- __city_id (str)__: OpenWeather city ID
- __lat_lon (array of str)__: the first item is the latatude and the second is the longitude
- __country_code (str)__: example 'us' or 'uk'

<h3 id="weather.API.forecast">forecast</h3>

```python
API.forecast(self, zip_code=None, city_name=None, city_id=None, lat_lon=None, country_code='us')
```

get the 5 day, 3 hour forecast a location. Must specifiy one of the following combinations:
- zip_code and country_code
- city_name and country_code
- city_id
- lat_lon

__Arguments__

- __zip_code (str)__: zip code of location
- __city_name (str)__: name of the City such as 'London'
- __city_id (str)__: OpenWeather city ID
- __lat_lon (array of str)__: the first item is the latatude and the second is the longitude
- __country_code (str)__: example 'us' or 'uk'

