from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import AuthenticationForm 
from django.http import HttpResponse 
 
def login_view(requestdboperation_app): 
    if request.method == 'POST': 
        form = AuthenticationForm(request, data=request.POST) 
        if form.is_valid(): 
            username = form.cleaned_data['username'] 
            password = form.cleaned_data['password'] 
            user = authenticate(request, username=username, password=password) 
            if user is not None: 
                login(request, user) 
                return redirect('home') 
            else: 
                return HttpResponse("Invalid login credentials.", status=400) 
    else: 
        form = AuthenticationForm() 
 
    return render(request, 'registration/login.html', {'form': form}) 
 
def home_view(request):
    if not request.user.is_authenticated: 
        return redirect('login')  # Redirect to login if not authenticated 
    return render(request, 'registration/home.html') 
 
def logout_view(request): 
    logout(request) 
    return redirect('login') 