from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from django.contrib.auth.models import User

#Checking if user is authenticated
class check_if_user_is_authenticated(LoginRequiredMixin, View):
    login_url='user_auth_app:login'

class UserProfileMiddleware():

    def render_user_profile(request, template_name):
        return render(request, template_name)

    def change_user_password(self, form):
        current_password = form.cleaned_data.get('password1')
        new_password = form.cleaned_data.get('password2')
        user = User.objects.get(pk=self.request.user.id)
        if user.check_password(current_password):
            user.set_password(new_password)
            user.save()
            messages.add_message(self.request, messages.SUCCESS, 'Your password has been changed')
            return redirect('user_profile_app:profile')
        else:
            messages.add_message(self.request, messages.ERROR, 'Invalid current password')
            return redirect('user_profile_app:password_change')