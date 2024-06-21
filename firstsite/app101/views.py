from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Item

# Create your views here.
def index(request):
    return HttpResponse('This is index page for the app.')


def home(request):
    template = loader.get_template('app101/home.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def item(request):
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'app101/item.html', context)

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'app101/detail.html', context)