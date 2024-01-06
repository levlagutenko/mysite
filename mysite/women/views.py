from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

menu =['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

class MyClass:
    def __int__(self, a, b):
        self.a = a
        self.b = b

def index(request):
    #t = render_to_string('women/index.html')
    #return HttpResponse(t)
    data = {
        'title': 'Самая главная страница',
        'menu': menu,
        'float': 77.5,
        'lst': [1,2,3,'trrtr', False],
        'set': {1,2,3,4,4,5,},
        'dict':{'key_1': 'value_1', 'key_2': 'value_2'},
        'obj': MyClass
    }

    return render(request, 'women/index.html', context=data)

def about(request):
    return render(request, 'women/about.html', {'title': 'Информация'})

def categories(request, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>id: {cat_id}</p>')

def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>')

def archive(request, year):
    if year > 2023:
        uri = reverse('cat', args=('music', ))
        return HttpResponseRedirect(uri)
    return HttpResponse(f'<h1>Архив по годам</h1><p>slug: {year}</p>')

def page_not_found(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не найдена 404</h1>')