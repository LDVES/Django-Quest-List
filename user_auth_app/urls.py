from django.urls import path
from user_auth_app.views import UserLogin, UserRegister
from user_auth_app.views import logout_view

#Namespace for quests manager
app_name='user_auth_app'
urlpatterns = [
	path('login', UserLogin.as_view(), name='login'),
    path('register', UserRegister.as_view(), name='register'),
	path('logout', logout_view, name='logout'),
]
