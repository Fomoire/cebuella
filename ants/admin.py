from django.contrib import admin
from Cuebella.ants.models import *

class news_admin(admin.ModelAdmin):
    list_display = ('sw_id', 'n_date','coms')
    list_filter = ('n_date',)
    search_fields = ('n_text',)

class ds_comment(admin.ModelAdmin):
    list_display = ('c_text','sw_id')
    list_filter = ('c_time',)

class ds_commentator(admin.ModelAdmin):
    search_fields = ('sw_id',)
class ds_trd(admin.ModelAdmin):
    list_display = ('task','stat','active','work_done')

admin.site.register(new, news_admin)
admin.site.register(tag)
admin.site.register(thread_list, ds_trd)
admin.site.register(comment,ds_comment)
admin.site.register(commentator, ds_commentator)
