from django.http import HttpResponse
from django.template import loader
from .generate_csv import GenerateCsv
from django.shortcuts import render



def index(request, *args, **kwords):
    return render(request, 'main/index.html')

def complete(request, *args, **kwargs):
    context = {
        'genre': request.POST.get('genre'),
        'search_input': request.POST.get('search_word'),
        'file_name': request.POST.get('file_name'),
    }
    genre = context.get('genre')
    search_input = context.get('search_input')
    file_name = context.get('file_name')
    generate_csv = GenerateCsv(genre,search_input,file_name)
    generate_csv.Execute()
    return render(request, 'main/complete.html')
