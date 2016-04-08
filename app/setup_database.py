from models import Car, Manufacturer
from database import db
#import requests
import json

def create_cars(car_json):
	for car in car_json:
		car_model = Car(car['make'], car['model'], car['year'], car['price'], car['horsepower'])
		db.session.add(car_model)
		db.session.commit()

def create_manufacturers(manufacturer_json):
	for man in manufacturer_json:
		manufacturer_model = Manufacturer(man['name'], man['num_models'], man['avg_price'], man['max_car_id'], man['avg_horsepower'])
		db.session.add(manufacturer_model)
		db.session.commit()

def create_database():
	db.create_all()

	'''car_json = json.load(open('cars_list.json'))
	create_cars(car_json)

	manufacturer_json = json.load(open('makes_list.json'))
	create_manufacturers(manufacturer_json)'''

	with open('cars_list.json') as car_json:
		car_data = json.load(car_json)
	create_cars(car_data)

	with open('makes_list.json') as manufacurer_json:
		manufacturer_data = json.load(manufacturer_json)
	create_manufacturers(manufacturer_data)	