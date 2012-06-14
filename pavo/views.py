#!/usr/bin/env python
# -*- coding: utf-8 -*-
#       Copyright 2012 Linar <khasanshin.linar@gmail.com>

from datetime import datetime, timedelta
from time import time
from django.shortcuts import render_to_response
from django.db.models import Q
from django.core.cache import cache
import operator


from cebuella.pavo.forms import *
from cebuella.ants.models import *

def pavo(request):
    """
    Processing the request to data base from user.
    """
    
    if ('words' in request.GET):
        t = time()
        
        cache_key = request.GET['words'].replace(' ','')
        words = request.GET['words']
        cache_time = 1800
        result = cache.get(cache_key)
        if not result:
            # Получаем массив слов
            search_words = words.split(' ')
            qsearch_words = []
            for w in search_words:
                qsearch_words.append(Q(n_text__icontains = w))
            
            # Отыскиваем новости
            news = new.objects.filter(reduce(operator.and_,
                                                qsearch_words)).values('id')
            f = len(news)
            
            if news:

                # Находим комменты найденных новостей
                comments = []
                for ids in news:
                     comments+=(comment.objects.filter(
                                        n_id = ids['id']).values('c_time'))
                
                comments.sort()
                
                min = comments[0]['c_time']
                max = comments[-1]['c_time']

                #Отсчитываем комменты:
                delta = max - min
                dt = delta/40 # Шаг сравнения
                data = []
                k = 0
                step = min
                for tik in comments:
                    k += 1
                    if tik['c_time'] > step:
                        data.append(k)
                        step += dt
                t = time() - t
                t = round(t, 4)
                
                result = []
                cache.set(cache_key,[data, f, min, max, int(dt.total_seconds())], cache_time)
                
                return render_to_response('pavo_finded.html', {'finded':f,
                                                         'words': words,
                                                         'start': min,
                                                         'data':data,
                                                         'dt':int(dt.total_seconds()),
                                                         'end':max,
                                                         'time':t})
            else:
                t = time()-t
                t = round(t, 4)
                cache.set(cache_key,[[], f, '', '', ''], cache_time)
                return render_to_response('pavo_finded.html', {'finded':f,
                     'words': words,
                     'time':t}
                     )
        t = time()-t
        t = round(t, 4)
        return render_to_response('pavo_finded.html', {'finded':result[1],
                                                         'words': words,
                                                         'start': result[2],
                                                         'data':result[0],
                                                         'dt':result[4],
                                                         'end':result[3],
                                                         'time':t})
    #Поиск посторойка диаграммы появления новостей
    if ('news' in request.GET):
        t = time()
        # Получаем массив слов
        words = request.GET['news']
        search_words = words.split(' ')
        qsearch_words = []
        for w in search_words:
            qsearch_words.append(Q(n_text__icontains = w))
        
        
        # Отыскиваем новости
        news = []
        news += new.objects.filter(reduce(operator.and_, 
                                    qsearch_words)).values('n_date')
        f = len(news)

        if news:

            news.sort()
            min = news[0]['n_date']
            max = news[-1]['n_date']
            #Отсчитываем комменты:
            delta = max - min
            dt = delta/40 # Шаг сравнения
            data = []
            k = 0
            step = min
            for tik in news:
                k += 1
                if tik['n_date']>step:
                    data.append(k)
                    step += dt
            t = time() - t
            t = round(t, 4)
            return render_to_response('pavo_finded.html', {'finded':f,
                                                     'words': words,
                                                     'start': min,
                                                     'data':data,
                                                     'dt':int(dt.total_seconds()),
                                                     'end':max,
                                                     'time':t})
        else:
            t = time() - t
            t = round(t, 4)
            return render_to_response('pavo_finded.html', {'finded':f,
                                                            'words': words,
                                                            'time':t})
        
    
    newform = NewsTab()
    return render_to_response('user_form.html',{'newform':newform})
