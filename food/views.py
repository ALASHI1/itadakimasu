from django.shortcuts import render,get_object_or_404
import requests 
from food.models import Food
from django.conf import settings as conf_settings
from django.http import HttpResponse


API_KEYS = conf_settings.APIKEYS
# Create your views here.
def make_requests(url):
	response = 'not working'
	for i in API_KEYS:
		r = requests.get(url+i)
		response = r.json()
		if 'status' not in response:
			break
	return response


def home(request):
	url = f'https://api.spoonacular.com/food/jokes/random?apiKey='
	route = f'https://api.spoonacular.com/recipes/random?number=100&apiKey='
	response = make_requests(url)
	result = make_requests(route)
	return render(request,'index.html',{'result':result,'response':response})



def food(request):
	if request.method == 'GET':
		food_type = request.GET.get('title')
		URL = f'https://api.spoonacular.com/recipes/complexSearch?query={food_type}&addRecipeInformation=true&number=100&apiKey='
		LINK = f'https://api.spoonacular.com/food/videos/search?query={food_type}&number=6&apiKey='
		response = make_requests(URL)
		data = make_requests(LINK)
		return render(request,'food.html',{'response':response,'data':data})


def food_ingredients(request,food_id):
	URL = f'https://api.spoonacular.com/recipes/{food_id}/ingredientWidget.json?apiKey='
	link = f'https://api.spoonacular.com/recipes/{food_id}/information?apiKey='
	response =  make_requests(url=URL)
	data = make_requests(url=link)
	return render(request,'food_ingredients.html',{'response':response,'data':data})


def food_equipments(request,food_id):
	URL = f'https://api.spoonacular.com/recipes/{food_id}/equipmentWidget.json?apiKey='
	response = make_requests(url=URL)
	return render(request,'food_equipments.html',{'response':response})


def wine(request):
	link = f'https://api.spoonacular.com/food/wine/recommendation?wine=merlot&number=60&apiKey='
	data = make_requests(url=link)
	return render(request,'food_steps.html',{'data':data})

def about(request):
	return render(request,'about.html',{})

def hero(request):
	link = f'https://api.spoonacular.com/recipes/random?number=100&tags=vegetarian&apiKey='
	data = make_requests(url=link)
	return render(request,'hero.html',{'data':data})


def hero1(request):
	link = f'https://api.spoonacular.com/recipes/random?number=100&tags=gluten&apiKey='
	data = make_requests(url=link)
	return render(request,'hero.html',{'data':data})


def hero2(request):
	link = f'https://api.spoonacular.com/recipes/random?number=100&tags=vegan&apiKey='
	data = make_requests(url=link)
	return render(request,'hero.html',{'data':data})

def hero3(request):
	link = f'https://api.spoonacular.com/recipes/random?number=100&tags=dessert&apiKey='
	data = make_requests(url=link)
	return render(request,'hero.html',{'data':data})




def trial(request):
	API_ENDPOINT = 'https://api.spoonacular.com/users/connect?apiKey=640b389c08f94f7eaebca76a78add0bf'
	API_KEY = '640b389c08f94f7eaebca76a78add0bf'
	data = {"username": "bensh1","firstName": "ben2","lastName": "shi1",} 
	r = requests.post(API_ENDPOINT,json=data)
	pastebin_url = r.text
	return HttpResponse(pastebin_url,content_type='text/plain')

# GET https://api.spoonacular.com/recipes/{id}/ingredientWidget.json&apiKey=
# GET https://api.spoonacular.com/recipes/complexSearch
# https://api.spoonacular.com/food/products/search?query=yogurt&apiKey=API-KEY
# https://api.spoonacular.com/recipes/complexSearch?query=pasta&addRecipeInformation=true&apiKey={API_KEY}
# GET https://api.spoonacular.com/recipes/complexSearch
# https://api.spoonacular.com/recipes/id/analyzedInstructions/complexSearch?stepBreakdown=true&id=654959&apiKey={API_KEY}
# https://api.spoonacular.com/recipes/654959/analyzedInstructions?apiKey={API_KEY}










