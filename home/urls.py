from django.urls import path
from . import views

#Namespace for home sites
#Example: home:index
app_name='home'
urlpatterns = [
	path('', views.index, name='index')
]
