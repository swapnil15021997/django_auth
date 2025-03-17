from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.

@login_required
def home():
    pass


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_form = {
            'username' :'',
            'password1':'',
            'password2':''
        }
        form = UserCreationForm(initial=initial_form)
    return render(request, 'auth/register.html',{'form':form})



def login_view(request):
    if request.method == 'POST':

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")  # Redirect to home page after login
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    else:
        initial_form = {
            'username' :'',
            'password':''
        }
        form = AuthenticationForm(initial=initial_form)
    return render(request, 'auth/login.html',{'form':form})

# @login_required()
def dashboard(request):
    return render(request,'layouts/app.html')

def logout_view(request):
    logout(request)
    return redirect('login')