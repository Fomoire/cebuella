#!/usr/bin/env python
# -*- coding: utf-8 -*-
#       Copyright 2012 Linar <khasanshin.linar@gmail.com>

import datetime
from Queue import Queue
from grab import DataNotFound, GrabNetworkError
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from cebuella.ants.models import *
from anthill.ant import vk_a
from anthill.an_ant import f_analys_a
from anthill.linkload import linkload
from cebuella.ants.forms import *


def queen(request):
    """
    This function fills the task stack and start threads, also they
    returns page of administrator form.
    """
    
    thr_str = thread_list.objects.filter()
    tabform = TabThreads()
    addform = AddThreads()
    addanform = AddAnThreads()
    admin = False
    if request.user.is_authenticated():
        admin = True

        #Processing the post request
        if request.method == 'POST':
            
            if 'open' in request.POST.keys():
                thread_list.objects.create(stat = False,
                                            task = 'New one',
                                            active = True,
                                            work_done = 0,
                                            )
                return HttpResponseRedirect('/queen/')
            checkbox_list = [int(x.replace('checkbox_','')) for x in request.POST if x.startswith('checkbox_')]                                    
            if 'do' in request.POST.keys() and checkbox_list:

                if request.POST['whatdo']=='':
                    return HttpResponseRedirect('/queen/')
                    
                elif request.POST['whatdo']=='delete_selected':
                    if thr_str:
                        for thr in thr_str:
                            if thr.id in checkbox_list:
                                thr.delete()
                                
                elif request.POST['whatdo']=='close_selected':
                    if thr_str:
                        for thr in thr_str:
                            if thr.id in checkbox_list:
                                thr.active = False
                                thr.save()
                                
                elif request.POST['whatdo']=='zero_selected':
                    if thr_str:
                        for thr in thr_str:
                            if thr.id in checkbox_list:
                                thr.work_done = 0
                                thr.save()
                elif request.POST['whatdo']=='on_selected':
                    if thr_str:
                        for thr in thr_str:
                            if thr.id in checkbox_list:
                                thr.active = True
                                thr.save()
                                
                return HttpResponseRedirect('/queen/')
                    
            #Processing of the initiation form of threads
            if 'add' in request.POST.keys():
                addform = AddThreads(request.POST)
                if addform.is_valid():
                    formdata = addform.cleaned_data
                    site = formdata['link']
                    thr_l = formdata['threads']
                    if formdata['limit']!=None:
                        limit = formdata['limit']
                    else:
                        limit = 0

                    if 'vk.com' in site:
                        # Trying to get a number of news in the group
                        try:
                            p=linkload(site)
                            link = site.replace('vk.com','')
                            lo = p.xpath_list('/html/body//a[@class="pg_lnk fl_l"]'
                            )[-1].get('href').replace(link+'?offset=','')
                            if lo!='':
                                lo=int(lo)
                            else:
                                return
                        #Обрабатываем исключение - "Ничего нет" и ошибка сети
                        except DataNotFound, GrabNetworkError:
                            lo = 0
                            pass
                            
                        #Кидаем в базу заданий ссылки с оффсетом
                        if limit * 20 > lo or limit == 0:
                            limit = lo
                        else:
                            limit *= 20
                        f_tasks = Queue()
                        for i in xrange(0, limit, 20):
                            lin = site + '?offset=' + str(i)
                            f_tasks.put(lin)
                        
                        #Получаем строчку из таблички потоков, для контроля и учета
                        # и запускаем потоки
                        thre = thread_list.objects.filter(active = True, stat = False)
                        for t in xrange(len(thre)):
                            if t + 1 <= thr_l:
                                thre[t].stat = True
                                thre[t].save()
                                ant_t = vk_a(f_tasks, thre[t])
                                ant_t.start()
                    return HttpResponseRedirect('/queen/')

            if 'addan' in request.POST.keys():
                addanform = AddAnThreads(request.POST)
                if addanform.is_valid():
                    formdata = addanform.cleaned_data
                    if formdata['number_of_an']!=None:
                        num = formdata['number_of_an']
                    else:
                        num = 'all'
                    
                    if formdata['from_date'] != None:
                        from_date = formdata['from_date']
                    else:
                        from_date = datetime.datetime.min
                    
                    if formdata['to_date'] != None:
                        to_date = formdata['to_date']
                    else:
                        to_date = datetime.datetime.now()
                    news = new.objects.filter(n_date__gte = from_date)# text_vector = None)
                    news = news.exclude(n_date__gte=to_date)
                    
                    if num != 'all':
                        news = news[:num]
                    if news.count != 0:
                        antask = Queue()
                        for i in news:
                            antask.put((i,'n'))
                            comments = comment.objects.filter(n_id = i.id)
                            for c in comments:
                                antask.put((c,'c'))
                                
                        
                        thre = thread_list.objects.filter(active = True, stat = False)
                        print 'Дошел'
                        #Start threads
                        tr = formdata['threads']
                        for i in xrange(len(thre)):
                            if i+1 <= tr:
                                thre[i].stat = True
                                thre[i].save()
                                th = f_analys_a(antask, thre[i])
                                th.run()

                    return HttpResponseRedirect('/queen/')
        
        return render_to_response('admin_control.html',
                {'thr_str':thr_str, 'addform': addform,
                'tabform' : tabform, 'addanform': addanform,
                'admin':admin},
                context_instance=RequestContext(request))
    else:
        return render_to_response('main.html',{'admin':admin})
