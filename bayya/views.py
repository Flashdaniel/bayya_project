from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from .admin import UserCreationForm, LoginForm

def home(request):
 return render(request, 'home.html')


def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            user = authenticate(email=email, password=password)
            login(request, user)
            # return HttpResponseRedirect('bayy:contact')
    else:
        form = UserCreationForm()
    return render(request, "bayya/register.html", {"form": form})

def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    print('is_active worked')
                    redirect(reverse('bayya:index'))
                else:

                    Print('Account not active')
            else:
                print('some one tried to login')

    else:
        form = LoginForm()            
    return render(request, 'bayya/login.html', {'form': form})

def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse("bayya:index"))


def index(request):
    return render(request, 'bayya/index.html')

def about(request):
    context = {
        'about': 'about'
    }
    return render(request, 'bayya/about.html',context)

def services(request):
        context = {
            'services': 'services'
        }
        return render(request, 'bayya/services.html',context)

def pricing(request):
        context = {
            'pricing': 'pricing'
        }
        return render(request, 'bayya/pricing.html',context)

def faq(request):
        context = {
            'faq': 'faq'
        }
        return render(request, 'bayya/faq.html',context)

def terms_of_services(request):
        context = {
            'terms_of_services': 'terms_of_services'
        }
        return render(request, 'bayya/terms-of-services.html',context)

def contact(request):
        context = {
            'contact': 'contact'
        }
        return render(request, 'bayya/contact.html',context)
