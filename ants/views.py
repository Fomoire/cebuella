# Create your views here.
from django.shortcuts import render_to_response
from Cuebella.ants.models import *

def current_datetime(request):
    now = down_site.objects.all()
    return render_to_response('page1.html', {'current_date': now})
