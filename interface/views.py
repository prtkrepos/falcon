from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Create your views here.

def game(request):
	if(request.method == 'GET'):
		return render(request,'base.html')

def ajax_view(request):

	val = request.GET['value']
	val += 1
	from django.utils import simplejson
	return HttpResponse(simplejson.dumps(val))
