from django.urls import path
from user_profile_app.views import ProfileView

#Namespace for home sites
#Example: user_profile_app:index
app_name='user_profile_app'
urlpatterns = [
	path('profile', ProfileView.as_view(), name='profile'),
]
