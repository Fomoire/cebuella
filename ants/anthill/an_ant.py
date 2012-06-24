#-*- coding: utf-8 -*-

import threading
import nltk
from nltk.stem.snowball import RussianStemmer

from cebuella.ants.models import new, commentator,comment, thread_list

class f_analys_a(threading.Thread):

    def __init__(self, tasks, thre):
        self.tasks = tasks
        self.thre = thre
        self.stopwords = [u'—',u'#',u'–',u'эт',u"''",u'``',u'...',u'^',u':',u';',u'+',u'/',u'\\',u'.',u"'",u',',u')',u'(',u'!',u'$',u'*',u'=',u'_',u'-',u'?',u'"',u'%',u'а',u'е',u'и',u'ж',u'м',u'о',u'на',u'не',u'ни',u'об',u'но',u'он',u'мне',u'мои',u'мож',u'она',u'они',u'оно',u'мной',u'много',u'многочисленное',u'многочисленная',u'многочисленные',u'многочисленный',u'мною',u'мой',u'мог',u'могут',u'можно',u'может',u'можхо',u'мор',u'моя',u'моё',u'мочь',u'над',u'нее',u'оба',u'нам',u'нем',u'нами',u'ними',u'мимо',u'немного',u'одной',u'одного',u'менее',u'однажды',u'однако',u'меня',u'нему',u'меньше',u'ней',u'наверху',u'него',u'ниже',u'мало',u'надо',u'один',u'одиннадцать',u'одиннадцатый',u'назад',u'наиболее',u'недавно',u'миллионов',u'недалеко',u'между',u'низко',u'меля',u'нельзя',u'нибудь',u'непрерывно',u'наконец',u'никогда',u'никуда',u'нас',u'наш',u'нет',u'нею',u'неё',u'них',u'мира',u'наша',u'наше',u'наши',u'ничего',u'начала',u'нередко',u'несколько',u'обычно',u'опять',u'около',u'мы',u'ну',u'нх',u'от',u'отовсюду',u'особенно',u'нужно',u'очень',u'отсюда',u'в',u'во',u'вон',u'вниз',u'внизу',u'вокруг',u'вот',u'восемнадцать',u'восемнадцатый',u'восемь',u'восьмой',u'вверх',u'вам',u'вами',u'важное',u'важная',u'важные',u'важный',u'вдали',u'везде',u'ведь',u'вас',u'ваш',u'ваша',u'ваше',u'ваши',u'впрочем',u'весь',u'вдруг',u'вы',u'все',u'второй',u'всем',u'всеми',u'времени',u'время',u'всему',u'всего',u'всегда',u'всех',u'всею',u'всю',u'вся',u'всё',u'всюду',u'г',u'год',u'говорил',u'говорит',u'года',u'году',u'где',u'да',u'ее',u'за',u'из',u'ли',u'же',u'им',u'до',u'по',u'ими',u'под',u'иногда',u'довольно',u'именно',u'долго',u'позже',u'более',u'должно',u'пожалуйста',u'значит',u'иметь',u'больше',u'пока',u'ему',u'имя',u'пор',u'пора',u'потом',u'потому',u'после',u'почему',u'почти',u'посреди',u'ей',u'два',u'две',u'двенадцать',u'двенадцатый',u'двадцать',u'двадцатый',u'двух',u'его',u'дел',u'или',u'без',u'день',u'занят',u'занята',u'занято',u'заняты',u'действительно',u'давно',u'девятнадцать',u'девятнадцатый',u'девять',u'девятый',u'даже',u'алло',u'жизнь',u'далеко',u'близко',u'здесь',u'дальше',u'для',u'лет',u'зато',u'даром',u'первый',u'перед',u'затем',u'зачем',u'лишь',u'десять',u'десятый',u'ею',u'её',u'их',u'бы',u'еще',u'при',u'был',u'про',u'процентов',u'против',u'просто',u'бывает',u'бывь',u'если',u'люди',u'была',u'были',u'было',u'будем',u'будет',u'будете',u'будешь',u'прекрасно',u'буду',u'будь',u'будто',u'будут',u'ещё',u'пятнадцать',u'пятнадцатый',u'друго',u'другое',u'другой',u'другие',u'другая',u'других',u'есть',u'пять',u'быть',u'лучше',u'пятый',u'к',u'ком',u'конечно',u'кому',u'кого',u'когда',u'которой',u'которого',u'которая',u'которые',u'который',u'которых',u'кем',u'каждое',u'каждая',u'каждые',u'каждый',u'кажется',u'как',u'какой',u'какая',u'кто',u'кроме',u'куда',u'кругом',u'с',u'т',u'у',u'я',u'та',u'те',u'уж',u'со',u'то',u'том',u'снова',u'тому',u'совсем',u'того',u'тогда',u'тоже',u'собой',u'тобой',u'собою',u'тобою',u'сначала',u'только',u'уметь',u'тот',u'тою',u'хорошо',u'хотеть',u'хочешь',u'хоть',u'хотя',u'свое',u'свои',u'твой',u'своей',u'своего',u'своих',u'свою',u'твоя',u'твоё',u'раз',u'уже',u'сам',u'там',u'тем',u'чем',u'сама',u'сами',u'теми',u'само',u'рано',u'самом',u'самому',u'самой',u'самого',u'семнадцать',u'семнадцатый',u'самим',u'самими',u'самих',u'саму',u'семь',u'чему',u'раньше',u'сейчас',u'чего',u'сегодня',u'себе',u'тебе',u'сеаой',u'человек',u'разве',u'теперь',u'себя',u'тебя',u'седьмой',u'спасибо',u'слишком',u'так',u'такое',u'такой',u'такие',u'также',u'такая',u'сих',u'тех',u'чаще',u'четвертый',u'через',u'часто',u'шестой',u'шестнадцать',u'шестнадцатый',u'шесть',u'четыре',u'четырнадцать',u'четырнадцатый',u'сколько',u'сказал',u'сказала',u'сказать',u'ту',u'ты',u'три',u'эта',u'эти',u'что',u'это',u'чтоб',u'этом',u'этому',u'этой',u'этого',u'чтобы',u'этот',u'стал',u'туда',u'этим',u'этими',u'рядом',u'тринадцать',u'тринадцатый',u'этих',u'третий',u'тут',u'эту',u'суть',u'чуть',u'тысяч']
        threading.Thread.__init__(self)

    def run(self):
        """Try to frequently analyse sentences of news and comments"""
        print self.tasks.qsize()
        while self.tasks.empty() != True:
            task = self.tasks.get()
            self.thre.task = task[0].sw_id
            self.thre.save()
            self.thre = thread_list.objects.filter(id=self.thre.id)
            if self.thre:
                self.thre = self.thre[0]
                if self.thre.active == False:
                    self.tasks.put(task)
                    self.thre.stat = False
                    self.thre.task = 'Was Killed'
                    self.thre.work_done -= 1
                    self.thre.save()
                    print 'DEAD'
                    return False

            
            if task[1] == 'n':
                sentence = task[0].n_text
            else:
                sentence = task[0].c_text


            tokens = nltk.word_tokenize(sentence)
            st = RussianStemmer(ignore_stopwords=False)
            stem = '['
            for i in tokens:
                if not i in self.stopwords:
                    stemmed = st.stem(i)
                    if not stemmed in self.stopwords:
                        stem += "'" + stemmed + "',"
            stem = stem[:-1]
            stem+=']'
            
            if stem == ']':
                stem = '[]'
            
            task[0].text_vector = stem
            task[0].save()
            
            self.thre.task = task[0].sw_id
            self.thre.work_done += 1
            self.thre.save()
        
        self.thre.stat = False
        self.thre.task = 'Done'
        self.thre.save()
        print 'done'
        return False
