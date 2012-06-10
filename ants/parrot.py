#!/usr/bin/env python
# -*- coding: utf-8 -*-
#       Copyright 2012 Linar <khasanshin.linar@gmail.com>

from grab import Grab
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from cebuella.ants.models import *
import bingtrans

def get_access_token():
    """
    Get access token from datamarket.accesscontrol.windows.net
    """
    
    g_api = Grab()
    g_api.setup(post = {'grant_type':'client_credentials',
                        'client_id':'Fomoire',
                        'client_secret':'yO2bsq13X7KvDwxLIWVLjrgGvd/0jOBV/JFiJGSGtbk=',
                        'scope':'http://api.microsofttranslator.com'})
    g_api.go('https://datamarket.accesscontrol.windows.net/v2/OAuth2-13')

    api_token = eval(g_api.response.body)
    return api_token['access_token']
    
def parrot(request):
    """
    This function need to start analysis comments and news
    """
    coms = comment.objects.exclude(tr_text = None)
    print len(coms)

    for i in coms:
        print i.c_text, i.tr_text
    
    #api_key = get_access_token()
    #print api_key
    #bingtrans.set_app_id('Bearer '+api_key)
    #time_ex = datetime.now()
    
    #for i in coms:
        #if datetime.now()-time_ex > timedelta(minutes=9):
            #api_key = get_access_token()
            #bingtrans.set_app_id('Bearer '+api_key)
            #time_ex = datetime.now()
        #if len(i.c_text)<1000:
            #i.tr_text = bingtrans.translate(i.c_text, 'ru', 'en')
            #print i.tr_text
            #i.save()
        
        
    return render_to_response('parrot_page.html')
