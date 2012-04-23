"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

#from linkload import linkload
#
#linkload('vk.com')

import threading, time
a=2
class MyThread(threading.Thread):
    def __init__(self, t):
        self.t = t
        threading.Thread.__init__(self)
    def run ( self ):
        global a 
        a=a*a
        self.t = time.time() - self.t
        print self.t
c=time.time()
for x in xrange ( 28 ):
    g = MyThread(c)
    g.start()


