from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from .admin import UserCreationForm, LoginForm, UserProfileForm
from .models import MyUser, UserProfile
from django.core.exceptions import ObjectDoesNotExist



def home(request):
 return render(request, 'home.html')


@csrf_exempt
def validate_email(request):
    email = request.POST.get('email')
    data = {
        'is_taken': MyUser.objects.filter(email__iexact=email).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this email already exists.'
    return JsonResponse(data)


def sign_up(request):
    context = {
        'form': UserCreationForm(),
        'userProfileForm': UserProfileForm()
    }
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        userProfileForm = UserProfileForm(request.POST)
        if form.is_valid() and userProfileForm.is_valid():
            form.save()
            userProfileForm.save()
            email = form.cleaned_data.get("email")
            refered_email = userProfileForm.changed_data.get('referers_email')
            phone_number = userProfileForm.changed_data.get('phone_number')
            bank_name = userProfileForm.changed_data.get('bank_name')
            bit_add_or_bank_acct = userProfileForm.changed_data.get('bitcoin_add_or_bank_acct')

            try:
                user = MyUser.objects.get(email=email)
            except ObjectDoesNotExist:
                pass
            else:
                UserProfile.objects.create(user=user)
                password = form.cleaned_data.get("password1")
                user = authenticate(email=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect(reverse('bayya:index'))
        else:
            context['form'] = form
            context['userProfileForm'] = userProfileForm
            context["error"] = "Invalid Login Credentials"
    return render(request, "bayya/register.html", context)

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
                    return redirect(reverse('bayya:index'))
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
