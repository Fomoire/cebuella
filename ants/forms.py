#!/usr/bin/env python
# -*- coding: utf-8 -*-
#       
#       Copyright 2012 Linar <khasanshin.linar@gmail.com>

from django import forms

class AddAnThreads(forms.Form):
    number_of_an = forms.IntegerField(label='Количество обрабатываемых данных',required=False)
    threads = forms.IntegerField(label='Потоков')
    from_date = forms.DateField(label='C даты', required=False)
    to_date = forms.DateField(label='По дату', required=False)
    
    def clean_threads(self):
        thread = self.cleaned_data['threads']

        if thread > 10:
            raise forms.ValidationError("Слишком много потоков")
        return thread 

class AddThreads(forms.Form):
    link = forms.CharField(max_length=80, label='Ссылка')
    threads = forms.IntegerField(label='Потоков')
    limit = forms.IntegerField(label='Предел листов', required=False)
    
    def clean_threads(self):
        thread = self.cleaned_data['threads']

        if thread > 10:
            raise forms.ValidationError("Слишком много потоков")
        return thread
        
    def clean_link(self):
        link = self.cleaned_data['link']
        
        if 'http' in link:
            raise forms.ValidationError("Введите без 'http://'")
        
        if not 'vk.com/wall-' in link:
            raise forms.ValidationError("Cсылки такого типа не поддерживаются")
        return link


class TabThreads(forms.Form):
    whatdo = forms.ChoiceField(choices = (('','------'), 
                        ('delete_selected','Удалить выбранные'),
                        ('close_selected','Убить выбранные'),
                        ('zero_selected', 'Обнулить выбранные'),
                        ('on_selected','Включить выбранные')
                        ))
