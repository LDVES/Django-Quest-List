from django.shortcuts import render
from django.views import View

#Rendering selected page
class PageView(View):
	#Path to template
	template_name = 'home/index.html'
	def get(self, request):
		return render(request, self.template_name)
