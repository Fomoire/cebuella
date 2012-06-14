#!/usr/bin/env python
# -*- coding: utf-8 -*-
#       Copyright 2012 Linar <khasanshin.linar@gmail.com>
import datetime

def am_pm(st):
    """
    Interpretation to 24 hours.
    """
    
    if ' am' in st:
        r = st.replace(' am','')
        if '|' in r:
            r=r.replace('|','')
        mt = r.split(':')
        return (int(mt[0]),int(mt[1]))
    if ' pm' in st:
        r = st.replace(' pm','')
        if '|' in r:
            r=r.replace('|','')
        mt = r.split(':')
        if int(mt[0])==12:
            mt[0]=-12
        return (int(mt[0])+12,int(mt[1]))

def date_interp(times):
    """
    Translating string date to datetime type.
    """
    
    tim_d=[]
    for i in times:
        f = False
        if 'Today at ' in i:
            y = i.replace('Today at ','')
            h = am_pm(y)
            time = datetime.datetime.now()
            time = time.replace(hour=h[0],minute = h[1])
            tim_d.append(time)
            f = True
            
        if 'Yesterday at ' in i:
            y = i.replace('Yesterday at ','')
            h = am_pm(y)
            time = datetime.datetime.now() - datetime.timedelta(days=1)
            time = time.replace(hour=h[0],minute = h[1])
            tim_d.append(time)
            f = True
        
        if not f:
            try:
                if '|' in i:
                    time = datetime.datetime.strptime(i,'%d %b at %I:%M %p|')
                else:
                    time = datetime.datetime.strptime(i,'%d %b at %I:%M %p')
                time = time.replace(year = datetime.datetime.now().year)
                tim_d.append(time)
            except ValueError:
                try:
                    if '|' in i:
                        time = datetime.datetime.strptime(i,'%b %d, %Y at %I:%M %p|')
                    else:
                        time = datetime.datetime.strptime(i,'%b %d, %Y at %I:%M %p')
                    tim_d.append(time)
                except ValueError:
                    return False
    return tim_d
            
            
            
            
