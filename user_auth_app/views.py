from django.shortcuts import render, reverse, redirect
from django.views import View
from user_auth_app.forms import UserLoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class UserLogin(View):
    def get(self, request):
        form = UserLoginForm
        return render(request, 'user_auth_app/forms/user_login_form.html', { 'form' : form })
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('quests_manager:index')
        else:
            form = UserLoginForm
            return redirect('user_auth_app:login')

class UserRegister(View):
    template_name = 'user_auth_app/forms/user_register_form.html'
    def get(self, request):
        form = UserCreationForm
        return render(request, self.template_name, {'form' : form})
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
