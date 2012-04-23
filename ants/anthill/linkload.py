# -*- coding: utf-8 -*-
'''
Created on 24.01.2012
Функция скачивания страницы
@author: linar
'''
from grab import Grab

def linkload(link):
    g = Grab()
    g.setup(hammer_mode=True, 
            hammer_timeouts=((30,30),(60,60),(120,120)),
             proxy='proxy.edu.ugrasu:3129',
             proxy_type='http',
             connect_timeout=5,
             timeout=5,
#proxy.edu.ugrasu:3129
             )
    g.go(link)
    return g
