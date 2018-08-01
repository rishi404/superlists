from django.http import HttpRequest
from django.shortcuts import render, redirect

from lists.models import Item


def home_page(request: HttpRequest):
    if request.method == 'POST':
        item: Item = Item()
        item.text = request.POST['item_text']
        item.save()
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'lists/home.html', {
        'items': items,
    })
