# Create your views here.
from django.shortcuts import render_to_response
from cebuella.ants.models import new, comment

def maine(request):
    admin = False
    if request.user.is_authenticated(): admin = True
    n = new.objects.count
    c = comment.objects.count
    
    return render_to_response('main.html',{'admin':admin, 'news':n, 'comments': c})
