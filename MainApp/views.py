from django.http import Http404, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404
from MainApp.models import Snippet
from django.http import HttpResponseNotFound, HttpResponseServerError
from MainApp.forms import SnippetForm


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
    # Создаем пустую форму при запросе GET
    if request.method == 'GET':
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form
            }  
        return render(request, 'pages/add_snippet.html', context)

    # Получаем данные из формы и на их основе создаем новый сниппет, сораняя его в БД

    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            # GET / snippets list
            return redirect('snippets-list')
        return render(request, 'pages/add_snippet.html', context={'form': form})







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


def create_snippet(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            # GET / snippets list
            return redirect('snippets-list')
        return render(request, 'pages/add_snippet.html', context={'form': form})

    return HttpResponseNotAllowed(["POST"], 'You must make POST  request to add snippe.')
    

    
   