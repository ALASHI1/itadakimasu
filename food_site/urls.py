"""food_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from food import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('food/',views.food,name='food'),
    path('food/ingredients/<int:food_id>',views.food_ingredients,name='food_ingredients'),
    path('food/equipments/<int:food_id>',views.food_equipments,name='food_equipments'),
    path('food/wine/',views.wine,name='wine'),
    path('food/about/',views.about,name='about'),
    path('food/hero/',views.hero,name='hero'),
    path('food/hero1/',views.hero1,name='hero1'),
    path('food/hero2/',views.hero2,name='hero2'),
    path('food/hero3/',views.hero3,name='hero3'),
    path('food/trial/',views.trial,name='trial'),


]
