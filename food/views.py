from django.shortcuts import render,get_object_or_404
import requests 
from food.models import Food
from django.conf import settings as conf_settings
from django.http import HttpResponse


# Create your views here.
def home(request):
	API_KEY=conf_settings.APIKEY
	url = f'https://api.spoonacular.com/food/jokes/random?apiKey={API_KEY}'
	route = f'https://api.spoonacular.com/recipes/random?number=100&apiKey={API_KEY}'
	x = requests.get(route)
	r = requests.get(url)
	response = r.json()
	result = x.json()
	return render(request,'index.html',{'result':result,'response':response,'apiKey':API_KEY})



def food(request):
	API_KEY=conf_settings.APIKEY
	if request.method == 'GET':
		food_type = request.GET.get('title')
		URL = f'https://api.spoonacular.com/recipes/complexSearch?query={food_type}&addRecipeInformation=true&number=100&apiKey={API_KEY}'
		LINK = f'https://api.spoonacular.com/food/videos/search?query={food_type}&number=6&apiKey={API_KEY}'
		r = requests.get(URL)
		s = requests.get(LINK)
		response = r.json()
		data = s.json()
		return render(request,'food.html',{'response':response,'data':data,'apiKey':API_KEY})


def food_ingredients(request,food_id):
	API_KEY=conf_settings.APIKEY
	URL = f'https://api.spoonacular.com/recipes/{food_id}/ingredientWidget.json?apiKey={API_KEY}'
	link = f'https://api.spoonacular.com/recipes/{food_id}/information?apiKey={API_KEY}'
	r = requests.get(url=URL)
	k = requests.get(url=link)
	response = r.json()
	data = k.json()
	return render(request,'food_ingredients.html',{'response':response,'data':data,'apiKey':API_KEY})


def food_equipments(request,food_id):
	API_KEY=conf_settings.APIKEY
	URL = f'https://api.spoonacular.com/recipes/{food_id}/equipmentWidget.json?apiKey={API_KEY}'
	r = requests.get(url=URL)
	response = r.json()
	return render(request,'food_equipments.html',{'response':response,'apiKey':API_KEY})


def wine(request):
	API_KEY=conf_settings.APIKEY
	link = f'https://api.spoonacular.com/food/wine/recommendation?wine=merlot&number=60&apiKey={API_KEY}'
	k = requests.get(url=link)
	data = k.json()
	return render(request,'food_steps.html',{'data':data,'apiKey':API_KEY})

def about(request):
	return render(request,'about.html',{})

def hero(request):
	API_KEY=conf_settings.APIKEY
	link = f'https://api.spoonacular.com/recipes/random?number=100&tags=vegetarian&apiKey={API_KEY}'
	k = requests.get(url=link)
	data = k.json()
	return render(request,'hero.html',{'data':data, 'apiKey':API_KEY})


def hero1(request):
	API_KEY=conf_settings.APIKEY
	link = f'https://api.spoonacular.com/recipes/random?number=100&tags=gluten&apiKey={API_KEY}'
	k = requests.get(url=link)
	data = k.json()
	return render(request,'hero.html',{'data':data,'apiKey':API_KEY})


def hero2(request):
	API_KEY=conf_settings.APIKEY
	link = f'https://api.spoonacular.com/recipes/random?number=100&tags=vegan&apiKey={API_KEY}'
	k = requests.get(url=link)
	data = k.json()
	return render(request,'hero.html',{'data':data,'apiKey':API_KEY})

def hero3(request):
	API_KEY=conf_settings.APIKEY
	link = f'https://api.spoonacular.com/recipes/random?number=100&tags=dessert&apiKey={API_KEY}'
	k = requests.get(url=link)
	data = k.json()
	return render(request,'hero.html',{'data':data,'apiKey':API_KEY})




def trial(request):
	API_ENDPOINT = 'https://api.spoonacular.com/users/connect?apiKey=640b389c08f94f7eaebca76a78add0bf'
	API_KEY = '640b389c08f94f7eaebca76a78add0bf'
	data = {"username": "bensh1","firstName": "ben2","lastName": "shi1",} 
	r = requests.post(API_ENDPOINT,json=data)
	pastebin_url = r.text
	return HttpResponse(pastebin_url,content_type='text/plain')

# GET https://api.spoonacular.com/recipes/{id}/ingredientWidget.json&apiKey={API_KEY}
# GET https://api.spoonacular.com/recipes/complexSearch
# https://api.spoonacular.com/food/products/search?query=yogurt&apiKey=API-KEY
# https://api.spoonacular.com/recipes/complexSearch?query=pasta&addRecipeInformation=true&apiKey={API_KEY}
# GET https://api.spoonacular.com/recipes/complexSearch
# https://api.spoonacular.com/recipes/id/analyzedInstructions/complexSearch?stepBreakdown=true&id=654959&apiKey={API_KEY}
# https://api.spoonacular.com/recipes/654959/analyzedInstructions?apiKey={API_KEY}










