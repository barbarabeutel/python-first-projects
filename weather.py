import requests


api_key = '64360b781f2d2daeea70ba587eb88677'
city = 'Orlando'
url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric"

request = requests.get(url)
json = request.json()


description = json.get('weather')[0].get("description")
print("Today's forecast is of ", description,".",sep='')

temp_min = json.get('main').get("temp_min")
temp_max = json.get('main').get("temp_max")
print("With minimum temperatures reaching ", temp_min,"°C", " and maximum ", temp_max,"°C.", sep='')




