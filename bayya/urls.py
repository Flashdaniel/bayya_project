from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'bayya'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('pricing/', views.pricing, name='pricing'),
    path('faq/', views.faq, name='faq'),
    path('terms_of_services/', views.terms_of_services, name='terms_of_services'),
    path('contact/', views.contact, name='contact'),
    path('sign_up/', views.sign_up, name='signup'),
    path('login/', views.login_page, name='login'),
    # path('login/', auth_views.login, {'template_name': 'bayya/login.html'}, name='login'),

]
