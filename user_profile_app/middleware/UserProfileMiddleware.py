from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
#Checking if user is authenticated
class check_if_user_is_authenticated(LoginRequiredMixin, View):
    login_url='user_auth_app:login'

class UserProfileMiddleware():

    def render_user_profile(request, template_name):
        return render(request, template_name)
