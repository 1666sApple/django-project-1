from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView

# Create your views here.
def index(request):
    return HttpResponse('This is index page for the app.')

def home(request):
    template = loader.get_template('app101/home.html')
    context = {}
    return HttpResponse(template.render(context, request))

# Function Based View
# def item(request):
#     items = Item.objects.all()
#     context = {
#         'items': items,
#     }
#     return render(request, 'app101/item.html', context)

# Class based view
class Itemclassview(ListView):
    model = Item
    template_name = 'app101/item.html'
    context_object_name = 'items'

def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'app101/detail.html', context)

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app101:home')
    else:
        form = ItemForm()
    return render(request, 'app101/create_item.html', {'form': form})

def edit_item(request, id):
    item = get_object_or_404(Item, id=id)
    form = ItemForm(request.POST or None, instance=item)
    
    if form.is_valid():
        form.save()
        return redirect('app101:item')
    
    return render(request, 'app101/create_item.html', {'form': form, 'item': item})

def delete_item(request, id):
    item = get_object_or_404(Item, id=id)
    
    if request.method == 'POST':
        item.delete()
        return redirect('app101:item')
    
    return render(request, 'app101/delete_item.html', {'item': item})

def search(request):
    query = request.GET.get('query')
    if query:
        results = Item.objects.filter(name__iexact=query)
    else:
        results = Item.objects.none()

    return render(request, 'app101/search_results.html', {'results': results, 'query': query})
