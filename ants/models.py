#-*- coding: utf-8 -*-
from django.db import models

class thread_list(models.Model):
    stat = models.BooleanField()
    work_done = models.IntegerField(null=True)
    task = models.TextField(null=True)
    active = models.BooleanField()
    
# Тэги
class tag_list(models.Model):
    tg_text = models.CharField(max_length=200)

# Новости 
class new(models.Model):
    n_text = models.TextField() # Текст новости оригинальный
    n_date = models.DateTimeField() # Дата публикации
    tr_text = models.TextField(null=True) # Текст переведенный на англ
    sw_id = models.CharField(max_length=80) # ID в соцсети по совместительсту часть кода обращения
    text_vector = models.TextField(null=True) # Вектор кода
    coms = models.IntegerField(null=True)
    likes = models.IntegerField(null=True)
    def __unicode__(self):
        return self.sw_id

#Отношение многие ко многим
class tag(models.Model):
    tg_id = models.ForeignKey(tag_list, null=True)
    n_id = models.ForeignKey(new, null=True)

# Данные комментатора
class commentator(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),)
    b_day = models.CharField(max_length=80, null=True)
    r_city = models.CharField(max_length=120,null=True)
    f_city = models.CharField(max_length=120,null=True)
    study = models.TextField(null=True)
    music = models.TextField(null=True)
    books = models.TextField(null=True)
    religion = models.TextField(null=True)
    polit_conv = models.TextField(null=True)
    films = models.TextField(null=True)
    sex = models.CharField(null=True, max_length=1, choices=GENDER_CHOICES)
    sw_id = models.CharField(max_length=80)
    def __unicode__(self):
        return self.sw_id

# Комментарий
class comment(models.Model):
    cr_id = models.ForeignKey(commentator)
    n_id = models.ForeignKey(new)
    c_text = models.TextField()
    tr_text = models.TextField(null=True)
    sent_indic = models.FloatField(null=True)
    sw_id = models.CharField(max_length=80)
    c_time = models.DateTimeField()
    likes = models.IntegerField(null=True)
