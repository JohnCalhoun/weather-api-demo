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

