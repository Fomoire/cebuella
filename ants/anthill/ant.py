#-*- coding: utf-8 -*-

import threading, time
from grab import GrabNetworkError, DataNotFound
import datetime
from linkload import linkload
from cebuella.ants.models import new, commentator,comment, thread_list
from date_interp import date_interp

class vk_a(threading.Thread):
    def __init__(self, tasks,thre):
        self.tasks = tasks
        self.thre = thre
        threading.Thread.__init__(self)

    def run ( self ):
        try:
            while (self.tasks.empty()!=True)&(self.thre.active == True):
                # Снимаем задачу из пула
                self.task_link = self.tasks.get()
                
                #Записывем задачу в строку контроля
                self.thre.task = self.task_link
                self.thre.work_done += 1
                self.thre.save()
                
                # Пробуем скачать страницу
                try:
                    self.gr = linkload(self.task_link)
                except GrabNetworkError:
                    self.tasks.put(self.task_link)
                    self.thre.stat = False
                    self.thre.task = 'Done With Errors'
                    self.thre.work_done -= 1
                    self.thre.save()
                    print 'DEAD'
                    return False

                n = self.gr.xpath_list('/html/body//div[@class="post"]')
                k = [ i.get('id').replace('post','') for i in n ] # Список айдишников новостей в листе
                
                for i in k: # Перебираем новости по внутренним ID
                    tr = new.objects.filter(sw_id=i)
                    
                    f1 = False # Флажок индикатор новой записи
                    if len(tr) == 0: # Проверяем нет ли в базе такой же новости
                        f1 = True
                        n_new = new()
                        n_new.sw_id = i
                    else:
                        n_new = tr[0]
                    try:
                        self.gr = linkload('vk.com/wall'+i)# Получаем страницу конкретной новости
                    except GrabNetworkError:
                        self.tasks.put(self.task_link)
                        self.thre.stat = False
                        self.thre.task = 'Done With Errors'
                        self.thre.work_done -= 1
                        self.thre.save()
                        print 'DEAD'
                        return False
                    
                    f2 = False # Флажок наличия косяков при парсинге
                    
                    try: # Пробуем парсить
                        new_text = self.gr.xpath(
                        '/html/body//div[@class="wall_post_text"]').text_content() #текст новости
                    except DataNotFound:
                        f2 = True
                        pass

                    if f2==False: # Не идем дальше если не парсится
                        if f1: n_new.n_text = new_text
                        print new_text

                        k=self.gr.xpath('/html/body//div[@class="summary"]'
                        ).text_content().split(' ')[0] # колличество комментариев
                        likes = self.gr.xpath('/html/body//div//span[@class="fw_like_count fl_l"]'
                        ).text_content() # Лайки новостей
                        if likes == '':
                            n_new.likes = 0
                        else:
                            n_new.likes = int(likes)
                        n_time = self.gr.xpath('/html/body//div[@class="fl_l fw_post_date"]'
                        )
                        n_new.n_date = date_interp([n_time.text_content()])[0].strftime("%Y-%m-%d %H:%M")
                        # Переводим кол-во комментов в инт, бывает что пусто, но комменты есть
                        if k!='':
                            k=k.replace(',','')
                            k=int(k)
                            n_new.coms=k
                        else:
                            n_new.coms=0
                            k=19
                        n_new.save()
                        
                        # Идем по страницам комментариев
                        for j in range(0,k,20): 
                            try:
                                self.gr = linkload('vk.com/wall'+i+'?offset='+str(j))
                            except GrabNetworkError:
                                self.tasks.put(self.task_link)
                                self.thre.stat = False
                                self.thre.task = 'Done With Errors'
                                self.thre.work_done -= 1
                                self.thre.save()
                                print 'DEAD'
                                return False
                            f3 = False # Индикатор косяков при парсинге
                            try: # Пробуем парсить комменты
                                posts_id = self.gr.xpath_list(
                                '/html/body//div[@class="fw_reply"]') # IDшники постов
                                print 'Постов - ', len(posts_id)
                                h = self.gr.xpath_list(
                                '/html/body//div//a[@class="fw_reply_thumb"]') # ссылки на комментаторов
                                print 'Комментаторов - ',len(h)
                                r = self.gr.xpath_list(
                                '/html/body//div[@class="fw_reply_text"]') # тексты комментов

                                li= self.gr.xpath_list(
                                '/html/body//div//span[@class="like_count fl_l"]') # like
                                
                                # Уроды из вконтакте сделали 2 варианта показа времени и оба тупые
                                times = self.gr.xpath_list(
                                '/html/body//div//span[@class="rel_date rel_date_needs_update"]') #Время поста
                                times_st = [ti.get('abs_time') for ti in times]
                                times = self.gr.xpath_list(
                                '/html/body//div//span[@class="rel_date"]')
                                for ti in times:
                                    times_st.append(ti.text_content())
                                
                                
                                times = date_interp(times_st)
                                    
                                if times == False:
                                    f3=True
                            except DataNotFound:
                                f3 = True
                                pass

                            if f3==False:
                                for i0 in range(len(h)): # Поехали по комментам страницы
                                    
                                    #А не отрубил ли админ активность
                                    self.thre = thread_list.objects.filter(id=self.thre.id)
                                    if self.thre:
                                        self.thre = self.thre[0]
                                        if self.thre.active == False:
                                            self.tasks.put(self.task_link)
                                            self.thre.stat = False
                                            self.thre.task = 'Was Killed'
                                            self.thre.work_done -= 1
                                            self.thre.save()
                                            print 'DEAD'
                                            return False
                                    else:
                                        return False
                                    
                                    #Проверяем на наличие коммента в базе
                                    id_sw = posts_id[i0].get('id')
                                    tr_t=comment.objects.filter(sw_id=id_sw) # Запрашиваем в базе комменты с таким же sw_id
                                    f4 = False # Флаг повторности коммента
                                    if len(tr_t)==0: 
                                        n_comment = comment()
                                        n_comment.sw_id = id_sw
                                        n_comment.n_id_id = n_new.id
                                        f4 = True
                                    else:
                                        n_comment = tr_t[0]
                                    if f4==True: # Если коммент новый
                                        f5 = False # Комментатор
                                        id_sw_c = h[i0].get('href') # Id комментатора в соцсети
                                        tr_c = commentator.objects.filter(sw_id=id_sw_c)
                                        
                                        if len(tr_c) == 0:
                                            f5 = True
                                            n_commentator = commentator()
                                            n_commentator.sw_id = id_sw_c
                                        else:
                                            n_commentator = tr_c[0]
                                        
                                        # ОООО погнали по комментатору
                                        if f5==True:
                                            try:
                                                self.gr = linkload('vk.com'+id_sw_c)
                                            except GrabNetworkError:
                                                self.tasks.put(self.task_link)
                                                self.thre.stat = False
                                                self.thre.task = 'Done With Errors'
                                                self.thre.work_done -= 1
                                                self.thre.save()
                                                print 'DEAD'
                                                return False
                                            f6=False
                                            try:
                                                print self.gr.xpath_text('/html/body//div/h1[@id="title"]')
                                                p = self.gr.xpath_list('/html/body//div[@class="label fl_l"]')
                                                s = self.gr.xpath_list('/html/body//div[@class="labeled fl_l"]')
                                            except DataNotFound:
                                                f6 = True
                                                pass
                                            if f6==False:
                                                for i1 in xrange(len(p)):
                                                    if p[i1].text_content() == 'Birthday:':
                                                            n_commentator.b_day = s[i1].text_content()
                                                    elif p[i1].text_content() == 'Hometown:':
                                                            if len(s[i1].text_content())<120:
                                                                n_commentator.r_city = s[i1].text_content()
                                                    elif p[i1].text_content() ==  'Current city:':
                                                            n_commentator.f_city = s[i1].text_content()
                                                    elif p[i1].text_content() == 'College or university:':
                                                            n_commentator.study = s[i1].text_content()
                                                    elif p[i1].text_content() == 'Department:':
                                                            n_commentator.study = n_commentator.study + ' ' + s[i1].text_content()
                                                    elif p[i1].text_content() == 'Major:':
                                                            n_commentator.study = n_commentator.study + ' ' + s[i1].text_content()
                                                    elif p[i1].text_content() == 'Favorite music:':
                                                            n_commentator.music = s[i1].text_content()
                                                    elif p[i1].text_content() == 'Favorite movies:':
                                                            n_commentator.films = s[i1].text_content()
                                                    elif p[i1].text_content() == 'Religious views:':
                                                            n_commentator.religion = s[i1].text_content()
                                                    elif p[i1].text_content() == 'Favorite books:':
                                                            n_commentator.books = s[i1].text_content()
                                                    elif p[i1].text_content() == 'Political views:':
                                                            n_commentator.polit_conv = s[i1].text_content()
                                            
                                        n_commentator.save() # Сохраняем
                                        
                                        n_comment.cr_id = n_commentator
                                            
                                        n_comment.c_text = r[i0].text_content()
                                        n_comment.c_time = times[i0].strftime("%Y-%m-%d %H:%M")

                                    if li[i0].text_content()!='': 
                                        n_comment.likes = int(li[i0].text_content())
                                    else: # тада 0
                                        n_comment.likes = 0
                                    n_comment.save()
                
                print '--------------------------ГОТОВААААААА-------------------------'
            
            self.thre.stat = False
            self.thre.task = 'Done All'
            self.thre.save()
        except:
            self.thre = thread_list.objects.filter(id=self.thre.id)
            if self.thre:
                self.thre = self.thre[0]
                if self.thre.active == False:
                    self.tasks.put(self.task_link)
                    self.thre.stat = False
                    self.thre.task = 'Was Killed'
                    self.thre.work_done -= 1
                    self.thre.save()
                    print 'DEAD'
                    return False
            else:
                return False
    
