from django.contrib.auth.views import LoginView
from django.shortcuts import render

from django.views.generic import TemplateView, CreateView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class IndexTemplateView(TemplateView):
    template_name = 'index.html'
    extra_context = {
        'title': 'Главная'
    }


class UserCreationView(CreateView):
    model = User
    template_name = 'common/user_registration_form.html'
    extra_context = {
        'title': 'Регистрация'
    }
    form_class = UserCreationForm
    success_url = '/'


class UserLoginView(LoginView):
    template_name = 'common/login.html'
    redirect_authenticated_user = '/'
