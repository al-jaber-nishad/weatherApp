from django.shortcuts import render
from django.http import HttpResponse

import urllib.request
import json
# Create your views here.

import time
from datetime import datetime


# importing module
from geopy import geocoders
from timezonefinder import TimezoneFinder
# initialize Nominatim API
def index(request):

  if request.method == 'POST':
    city = request.POST['city']
    source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ city +'&units=metric&appid=b88fbeb981238d623e7d46ac3e919392').read()

    list_of_data = json.loads(source)

    data = {
      'country_code' : str(list_of_data['sys']['country']),
      'coordinte' : str(list_of_data['coord']['lon']+list_of_data['coord']['lat']),
      'temp' : str(list_of_data['main']['temp']) + '° C',
      'pressure' : str(list_of_data['main']['pressure']),
      'humidity' : str(list_of_data['main']['humidity']) + '%',
      'main' : str(list_of_data['weather'][0]['main']),
      'description' : str(list_of_data['weather'][0]['description']),
      'icon' : list_of_data['weather'][0]['icon'],
      'wind' : str(round(list_of_data['wind']['speed'] * 3.6)),

      'city' : city.capitalize(),
    }
    

    return render(request, 'index.html', data)

  else:
    return render(request, 'index.html')




  