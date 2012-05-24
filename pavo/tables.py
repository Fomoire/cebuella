#!/usr/bin/env python
# -*- coding: utf-8 -*-
#       
#       Copyright 2012 Linar <khasanshin.linar@gmail.com>


from django.shortcuts import render_to_response
from datetime import datetime, timedelta
from cebuella.ants.models import new

def newslist(period, order):
    news = new.objects.filter(n_date__gte=datetime.now()-timedelta(days=period)).order_by(order)[:10]
    for n in news:
            n.sh=n.n_text[:80]+'...'
    return news

def tables(request, page):
    page = int(page)
    
    if page==1: #За неделю комм
        news = newslist(7,'-coms')
        str_l = 'За последюю неделю наиболее обсужаемы:'
    elif page==2:# За месяц ком
        news = newslist(30,'-coms')
        str_l = 'За последий месяц наиболее обсужаемы:'
    elif page==3:#За год ком
        news = newslist(365,'-coms')
        str_l = 'За последий год наиболее обсужаемы:'
    elif page==4:#За неделю лайков
        news = newslist(7,'-likes')
        str_l = 'За последюю неделю наиболее понравившиеся:'
    elif page==5:#За неделю лайков
        news = newslist(30,'-likes')
        str_l = 'За последий месяц наиболее понравившиеся:'
    elif page==6:#За неделю лайков
        news = newslist(365,'-likes')
        str_l = 'За последий год наиболее понравившиеся:'
    

    
    return render_to_response('tabl_page.html',{'news':news, 'str_l': str_l})
    
