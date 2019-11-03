import requests

class API():
    def __init__(self,api_key):
        self.api_key=api_key
        self.version="2.5"
        self.url_base="https://api.openweathermap.org/data/%s"%(self.version)
        pass

    def _params(self,zip_code=None,city_name=None,city_id=None,lat_lon=None,country_code="us"):
        if zip_code:
            return'zip=%s,%s&appid=%s'%(zip_code,country_code,self.api_key)
        elif city_name:
            return'q=%s,%s&appid=%s'%(city_name,country_code,self.api_key)
        elif city_id:
            return'id=%s&appid=%s'%(city_id,self.api_key)
        elif lat_lon:
            return'lat=%s&lon=%s&appid=%s'%(lat_lon[0],lat_lon[1],self.api_key)
        else:
            raise Exception('Must provide a location')


    def current(self,zip_code=None,city_name=None,city_id=None,lat_lon=None,country_code="us"):
        params=self._params(zip_code=zip_code,city_name=city_name,city_id=city_id,lat_lon=lat_lon,country_code=country_code)
        url=self.url_base+'/weather?%s'%(params)
        r = requests.get(url)
        return r.json()

    def forecast(self,zip_code=None,city_name=None,city_id=None,lat_lon=None,country_code="us"):
        params=self._params(zip_code=zip_code,city_name=city_name,city_id=city_id,lat_lon=lat_lon,country_code=country_code)
        url=self.url_base+'/forecast?%s'%(params)
        r = requests.get(url)
        return r.json()
