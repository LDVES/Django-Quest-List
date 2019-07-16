from django.urls import path
from home.views import PageView

#Namespace for home sites
#Example: home:index
app_name='home'
urlpatterns = [
	path('', PageView.as_view(template_name='home/index.html'), name='index'),
	path('about', PageView.as_view(template_name='home/about.html'), name='about'),
	path('contact', PageView.as_view(template_name='home/contact.html'), name='contact')
]
