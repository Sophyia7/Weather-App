import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
  url = 'https://api.openweathermap.org/data/2.5/forecast?q={}&units=imperial&appid=962b5f353015bab4e44d6a292c569cfa'
  city = 'Lagos'


  r = requests.get(url.format(city)).json()

  weather = {
    'city' : city ,
    'temperature' : r['main']['temp'] ,
    'description' : r['weather'][0]['description'],
    'icon' : r['weather'][0]['icon'] ,
  }

  print(weather)

  return render_template('weather.html')


