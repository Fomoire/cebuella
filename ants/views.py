# Create your views here.
from django.shortcuts import render_to_response

def maine(request):
    
    return render_to_response('maine.html')
