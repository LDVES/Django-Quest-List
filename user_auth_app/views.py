from django.urls import reverse_lazy

from django.shortcuts import redirect
from django.views.generic.edit import FormView
from user_auth_app.forms import UserLoginForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

#Custom Middleware
from .middleware.UserAuthMiddleware import UserAuthMiddleware


# Create your views here.
class UserLogin(FormView):
    template_name = 'user_auth_app/forms/user_login_form.html'
    form_class = UserLoginForm
    #Dependency Incjection of UserAuthMiddleware
    user_auth_middleware = UserAuthMiddleware
    #URL to redirect authenticated users
    redirect_url = 'quests_manager:index'
    success_url = reverse_lazy('quests_manager:index')

    #Checking if user is logged
    def get(self, request):
       return self.user_auth_middleware.redirect_user_if_authenticated(self, self.request)

    def form_valid(self, form):
       return self.user_auth_middleware.login_user(self, form)

class UserRegister(UserLogin):
    template_name = 'user_auth_app/forms/user_register_form.html'
    form_class = UserCreationForm

    def get(self, request):
        return self.user_auth_middleware.redirect_user_if_authenticated(self, self.request)

    #Getting data from Form and processing
    def form_valid(self, form):
        return self.user_auth_middleware.register_user(self, form)

#Logging out user
def logout_view(request):
    logout(request)
    return redirect('home:index')
