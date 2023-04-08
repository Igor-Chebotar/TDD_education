from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    '''домашная страница'''
    return render(request, 'home.html')
