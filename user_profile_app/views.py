from django.shortcuts import render, redirect, reverse
from django.views import View
from .middleware.UserProfileMiddleware import UserProfileMiddleware, check_if_user_is_authenticated
from .forms import ChangePasswordForm
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.
class ProfileView(check_if_user_is_authenticated, View):
    template_name = 'user_profile_app/index.html'
    user_profile_middleware = UserProfileMiddleware

    def get(self, request):
        return self.user_profile_middleware.render_user_profile(request, self.template_name)

class ChangePasswordView(check_if_user_is_authenticated, FormView):
    model = User
    template_name = 'user_profile_app/forms/password_change_form.html'
    form_class = ChangePasswordForm
    user_profile_middleware = UserProfileMiddleware


    def form_valid(self, form):
        return self.user_profile_middleware.change_user_password(self, form)
