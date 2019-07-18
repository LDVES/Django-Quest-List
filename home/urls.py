from django.urls import path
from home.views import PageView, AboutView, ContactView

#Namespace for home sites
#Example: home:index
app_name='home'
urlpatterns = [
	path('', PageView.as_view(), name='index'),
	path('about', AboutView.as_view(), name='about'),
	path('contact', ContactView.as_view(), name='contact'),
]
