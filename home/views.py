from django.shortcuts import render
from django.template import RequestContext

from django.views.generic import View

# Create your views here.
# view for main home page.
class Index(View):
	"""Handle get and post request separately for Index page"""
	template_name = 'home/index.html'
	context = {'title' : 'Home'}

	def get(self, request, *args, **kwargs):
		return render(request,
						self.template_name,
						self.context)
