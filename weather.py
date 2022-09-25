import requests

def get_weather_desc_and_temp():

    api_key = '64360b781f2d2daeea70ba587eb88677'
    city = 'Orlando'
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric"

    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {'description':description,'temp_min':temp_min,
            'temp_max':temp_max}

def main():
    #Print results
    weather_dict = get_weather_desc_and_temp()
    print("Today's forecast is of ", weather_dict.get('description'),".",sep='')
    print("With minimum temperatures reaching ", weather_dict.get('temp_min'),"°C",
    " and maximum ", weather_dict.get('temp_max'),"°C.", sep='')
main()




