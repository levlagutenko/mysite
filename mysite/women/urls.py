from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'), ######### http://127.0.0.1:5000
    path('about/', views.about, name='about'), ######### http://127.0.0.1:5000
    path('post/<int:post_id>/', views.show_post, name='post'),
    path('addpge/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
]