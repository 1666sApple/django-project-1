from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome! Account created for {username}!')
            login(request, user)
            return redirect('login')
        # else:
            # messages.error(request, 'Error creating account. Please try again.')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

# def login(request):
#     return render(request, 'users/login.html')
    
def logout_view(request):
    logout(request)
    context = {'message': 'You have been logged out.'}
    return render(request, 'users/logout.html', context)

@login_required
def profilepage(request):
    return render(request, 'users/profile.html')