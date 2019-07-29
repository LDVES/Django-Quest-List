from django.shortcuts import render
from django.views import View
from .middleware.UserProfileMiddleware import UserProfileMiddleware, check_if_user_is_authenticated

# Create your views here.
class ProfileView(check_if_user_is_authenticated, View):
    template_name = 'user_profile_app/index.html'
    user_profile_middleware = UserProfileMiddleware

    def get(self, request):
        return self.user_profile_middleware.render_user_profile(request, self.template_name)
