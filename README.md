# weather-api-demo

# Setup

## Install
```bash
git clone https://github.com/JohnCalhoun/weather-api-demo.git
cd weather-api-demo
make init
cp config.yml.example config.yml
```

## Configure
- create open weather account and get an API Key
https://openweathermap.org/guide
- open config.yml and replace `put_your_key_here` with your api key

## Example
```bash
./example.py
```

## Docs
see [here](./docs/markdown/doc.md) for details 

## Tests
```bash
make tests
```
