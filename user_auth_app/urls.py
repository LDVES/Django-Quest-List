from django.urls import path
from user_auth_app.views import UserLogin, UserRegister

#Namespace for quests manager
app_name='user_auth_app'
urlpatterns = [
	path('login', UserLogin.as_view(), name='login'),
    path('register', UserRegister.as_view(), name='register'),
]
