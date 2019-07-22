from django.shortcuts import render, reverse, redirect
from django.views import View
from django.views.generic.edit import FormView
from user_auth_app.forms import UserLoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class UserLogin(FormView):
    template_name = 'user_auth_app/forms/user_login_form.html'
    form_class = UserLoginForm
    success_url = 'quests'

    def form_valid(self, form):
        #Getting data from Form
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        #Checking credentials
        user = authenticate(username=username, password=password)
        if user:
            return super().form_valid(form)
        else:
            return redirect('user_auth_app:login')

class UserRegister(FormView):
    template_name = 'user_auth_app/forms/user_register_form.html'
    form_class = UserCreationForm

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('user_auth_app:login')
        else:
            return redirect('user_auth_app:register')
