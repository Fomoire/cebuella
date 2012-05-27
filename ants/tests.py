#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

#from linkload import linkload
#
#linkload('vk.com')

#import bingtrans

#bingtrans.set_app_id('Bearer 74AF7FB2744CA645CE842CCEF80E4EF631F6FE83')  # you can get your AppID at: http://www.bing.com/developers/
#print bingtrans.translate('Привет мир', 'ru', 'en')

#from grab import Grab

gr = Grab()
gr.setup(headers = {'Authorization':'Bearer UX2MHjmCwX6H5aE4aAaWcwqRgYSsQG7GFbg/vzfFGK4='})
url = 'http://api.microsofttranslator.com/V2/Http.svc/Translate?to=en&appId=&text=Привет'
gr.go(url)
print gr.response.body

#from microsofttranslator import Translator
#translator = Translator('TOrOfJtnPQ0gMt0sJF1IwZyRCKHGcS3enLKV1Noric7rXyOG-NdcVxADSHU9a_IHW')
#print translator.translate("Hello", "pt")
