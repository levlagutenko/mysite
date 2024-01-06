from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'), ######### http://127.0.0.1:5000
    path('about/', views.about, name='about'), ######### http://127.0.0.1:5000
    path('cat/<int:cat_id>/', views.categories, name= 'cat_id'), ######### http://127.0.0.1:5000/cat/1/
    path('cat/<slug:cat_slug>/', views.categories_by_slug, name='cat'), ######### http://127.0.0.1:5000/cat/guiupiuguigi/
    path('archive/<year4:year>/', views.archive, name='archive') ###### https://docs.djangoproject.com/en/5.0/topics/http/urls/
]