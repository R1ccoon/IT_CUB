from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Task
from .forms import Taskform


def index(request):
    posts = Task.objects.order_by('-id')
    return render(request, 'main/menu.html', {'title': 'Главная Страница',
                                               'posts': posts})




def about(request):
    pass


def post(request):
   pass


def success(request):
    pass
