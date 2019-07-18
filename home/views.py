from django.shortcuts import render
from django.views import View

#Rendering selected page
class PageView(View):
	#Path to template
	template_name = 'home/index.html'
	def get(self, request):
		return render(request, self.template_name)

#Child classes of PageView class		
class AboutView(PageView):
	template_name = template_name='home/about.html'
class ContactView(PageView):
	template_name='home/contact.html'