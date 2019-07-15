from django.shortcuts import render

#Rendering Homepage site
def index(request):
	return render(request, 'home/index.html')

#Rendering About Us site
def about(request):
	return render(request, 'home/about.html')

#Rendering Contact site
def contact(request):
	return render(request, 'home/contact.html')
