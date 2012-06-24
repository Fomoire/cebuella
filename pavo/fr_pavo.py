#!/usr/bin/env python
# -*- coding: utf-8 -*-
#       
#       Copyright 2012 Linar <khasanshin.linar@gmail.com>


from django.shortcuts import render_to_response
from datetime import datetime, timedelta
from cebuella.ants.models import *
from time import time
from nltk import FreqDist

from django.db.models import Q
from django.core.cache import cache
import operator


def fr_pavo(request):
    """Функция строит частотную таблицу"""
    
    admin = False
    if request.user.is_authenticated():
        admin = True

    if ('coms' in request.GET):
        t = time()
        
        cache_key = request.GET['coms'].replace(' ','')
        words = request.GET['coms']
        #cache_time = 1800
        #result = cache.get(cache_key)
        #if not result:
        # Получаем массив слов
        search_words = words.split(' ')
        qsearch_words = []
        for w in search_words:
            qsearch_words.append(Q(n_text__icontains = w))
        
        # Отыскиваем новости
        news = new.objects.filter(reduce(operator.and_,
                                            qsearch_words)).values('id')
        f = len(news)
        print f
        if news:

            # Находим комменты найденных новостей
            
            tokens = []
            for ids in news:
                 comments = comment.objects.filter(
                                    n_id = ids['id'])
                 comments = comments.exclude(text_vector=None)
                 comments = comments.values('text_vector')
                 
                 if comments:
                     for vec in comments:
                         try:
                            tokens += eval(vec['text_vector'])[1:]
                         except:
                             pass
                        
            rec = FreqDist(tokens)
            list = rec.items()[:15]
            str_l = u'Лексемы в комментариях'
            t = time() - t
            t = round(t, 4)
            return render_to_response('freq_page.html',{'admin':admin, 'lex':list, 'str_l':str_l, 'time': t})
        
    if ('news' in request.GET):
        t = time()
        
        cache_key = request.GET['news'].replace(' ','')
        words = request.GET['news']
        #cache_time = 1800
        #result = cache.get(cache_key)
        #if not result:
        # Получаем массив слов
        search_words = words.split(' ')
        qsearch_words = []
        for w in search_words:
            qsearch_words.append(Q(n_text__icontains = w))
        
        # Отыскиваем новости
        news = new.objects.filter(reduce(operator.and_,
                                            qsearch_words)).values('text_vector')
        f = len(news)
        print f
        
        if news:
            tokens = []
            # Находим комменты найденных новостей
            for vec in news:
                try:
                   tokens += eval(vec['text_vector'])
                except:
                    pass
                        
            rec = FreqDist(tokens)
            list = rec.items()[:15]
            str_l = u'Лексемы в новостях'
            t = time() - t
            t = round(t, 4)
        return render_to_response('freq_page.html',{'admin':admin, 'lex':list, 'str_l':str_l, 'time': t})
            
    
    return render_to_response('freq_ch.html',{'admin':admin})
