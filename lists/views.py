from django.http import HttpRequest
from django.shortcuts import render, redirect

from lists.models import Item


def home_page(request: HttpRequest):
    if request.method == 'POST':
        item: Item = Item()
        item.text = request.POST['item_text']
        item.save()
        return redirect('/lists/the-only-list/')

    return render(request, 'lists/home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'lists/list.html', {
        'items': items,
    })
