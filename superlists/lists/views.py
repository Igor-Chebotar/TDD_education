from django.shortcuts import render, redirect
from lists.models import Item, List
from django.views.decorators.csrf import requires_csrf_token, csrf_exempt, csrf_protect


@csrf_protect
def home_page(request):
    '''домашная страница'''
    return render(request, 'home.html')


@csrf_protect
def view_list(request, list_id):
    '''представление списка'''
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})


@csrf_protect
def new_list(request):
    '''новый список'''
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}')


@csrf_protect
def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_id}')
