from django.shortcuts import render
import requests

# Create your views here.

def home(request):
	return render(request, 'control_service/index.html', {})

def get_request(request):
	print(request.POST['rcode'])
	requests.get(url = 'http://10.0.0.6:8000/', params = {'action_code': request.POST['rcode']})
	return render(request, 'control_service/index.html', {})