# weather-api-demo
This is a small python library for interacting with the OpenWeather APIs. Currently the high level api supports the current weather and 5 day forecast endpoints (which are free) and the lower level request api can access the other endpoints.

for more info on the full OpenWeather API see [here](https://openweathermap.org/api)

## Install
```bash 
pip3 install git+https://github.com/JohnCalhoun/weather-api-demo.git
```

to setup local dev environment run:
```bash
git clone https://github.com/JohnCalhoun/weather-api-demo.git
cd weather-api-demo
make init
cp config.yml.example config.yml
```
then create OpenWeather account and get an API Key [Instructions](https://openweathermap.org/guide). Finally, open config.yml and replace `put_your_key_here` with your api key. The API key is loaded in the unit tests and example.py scripts.

## Usage
```bash
from weather import API
api=API("your-api-key-here")
print(api.current(zip_code="75094"))
```
for a more involved example see example.py

## Docs
see [here](http://weather-api-demo.s3-website-us-east-1.amazonaws.com/) for details 

## Tests
Unit tests are located in the ./tests folder and can be run by:
```bash
make tests
```
