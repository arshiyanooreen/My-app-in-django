from django.http import HttpResponse
import json

def main(request):
	message = { 'Message':'Hello World!'}
	return HttpResponse(json.dumps(message),content_type="application/json")

# Create your views here.
