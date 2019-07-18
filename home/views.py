from django.shortcuts import render
from django.views import View
from .models import Page

#Rendering selected page
class PageView(View):
	#Path to template
	template_name = 'home/index.html'
	page_name = "Homepage"
	def get(self, request):
		try:
			page = Page.objects.get(page_name=self.page_name)
			return render(request, self.template_name, { 'page' : page } )
		except:
			return render(request, self.template_name)

#Child classes of PageView class
class AboutView(PageView):
	template_name = template_name='home/about.html'
	page_name = "About_us"
class ContactView(PageView):
	page_name  = "Contact"
	template_name='home/contact.html'
