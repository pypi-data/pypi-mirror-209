import requests, pprint

# url = "http://api.openweathermap.org/data/2.5/forecast?q=Madrid&appid=1fbdb1902adb7476df1f87e8b5457a05"
# resp = requests.get(url)
# print(resp.text)
# print(resp.json())


class Weather:
    """
    Creates a Weather instance getting an API key as input
    and either a city name or lat and long coordinates.
    
    Package usage example:
    # Create a weather instance using a city name:
    # The API key below is not guaranteed to work.
    # Get your own API key from https://openweathermap.org
    # And wait a couple of hours for the API key to be activated
    >>> weather1 = Weather(apikey='1fbdb1902adb7476df1f87e8b5457a05', city='Athens')
    
    # Using latitude and longitude coordinates
    >>> weather2 = Weather(apikey='1fbdb1902adb7476df1f87e8b5457a05', lat=41.1, lon=-4.1)
    
    # Get complete weather data for the next 12 hours:
    >>> weather1.next_12h
    
    # Get simplified weather data for the next 12 hours:
    >>> weather2.next12h_simplified
    
    Sample URL to get sky condition icons:
    https://openweathermap.org/img/wn/10d@2x.png
    """
    def __init__(self, apikey,  city=None, lat=None, lon=None):
        url = "https://api.openweathermap.org/data/2.5/forecast"
        if city:
            resp = requests.get(f"{url}?q={city}&appid={apikey}&units=metric")
            self.data = resp.json()
        elif lat and lon:
            resp = requests.get(f"{url}?lat={lat}&lon={lon}&appid={apikey}&units=metric")
            self.data = resp.json()
        else:
            raise TypeError("provide either a city or a lat and lon arguments!")
        if resp.status_code != 200:
            raise ValueError(f"{self.data['message']}")

    def next_12h(self):
        """
        Returns 3-hour data for the next 12 hours as a dict
        Returns:
            dict: 3-hour data for the next 12 hours
        """
        return self.data['list'][:4]
    
    def next_12h_simplified(self):
        """
        Returns 3-hour data of date, temperature, and sky condition
        for the next 12 hours
        Returns:
            list: list of the next 12 hours data, containing tuples
            of the 3-hour data
        """
        simple_data = list()
        for dicty in self.next_12h():
            simple_data.append((dicty['dt_txt'],
                                dicty['main']['temp'],
                                dicty['weather'][0]['description'],
                                dicty['weather'][0]['icon']))
        return simple_data
