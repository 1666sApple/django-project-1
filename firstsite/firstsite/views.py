from django.shortcuts import render

def home(request):
    print("Rendering home.html")
    return render(request, 'home.html')