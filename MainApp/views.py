from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from MainApp.models import Snippet
from django.http import HttpResponseNotFound, HttpResponseServerError

  

def handler404(request, exception=None):
    """Обработчик ошибки 404."""
    response = render(request, 'pages/error.html', {})
    response.status_code = 404
    return response

def handler500(request):
    """Обработчик ошибки 500."""
    response = render(request, 'pages/error.html', {})
    response.status_code = 500
    return response



def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    context = {'pagename': 'Добавление нового сниппета'}   
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    snippets = Snippet.objects.all()
    context = {
        'pagename': 'Просмотр сниппетов',
        'snippets': snippets
        }
    return render(request, 'pages/view_snippets.html', context)


def snippet_detail(request, snippet_id):
    try:
        snippet = Snippet.objects.get(pk=snippet_id)
    except Snippet.DoesNotExist:
          return render(request, 'pages/error.html', {'message': 'Запрашиваемый сниппет не найден.'}, status=404)
         
    context = {
        'pagename': 'Просмотр сниппета',
        'snippet': snippet 
    }
    return render(request, 'pages/snippet_detail.html', context)


