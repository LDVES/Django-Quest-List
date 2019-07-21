from django.shortcuts import render, reverse, redirect
from django.views import View
from user_auth_app.forms import UserLoginForm
from django.contrib.auth import authenticate, login

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
