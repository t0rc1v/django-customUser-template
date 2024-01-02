from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from .forms import CustomUserCreationForm


def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(request, "Account successfully created!")    

            return redirect("login")
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form}) 

def login_user(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome {email} !!')
        else:
            messages.info(request, "Please enter a correct username and password. Note that both fields may be case-sensitive.")

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect("login")