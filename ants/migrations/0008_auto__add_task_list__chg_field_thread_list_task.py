# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'task_list'
        db.create_table('ants_task_list', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal('ants', ['task_list'])


        # Changing field 'thread_list.task'
        db.alter_column('ants_thread_list', 'task', self.gf('django.db.models.fields.TextField')(null=True))
    def backwards(self, orm):
        # Deleting model 'task_list'
        db.delete_table('ants_task_list')


        # Changing field 'thread_list.task'
        db.alter_column('ants_thread_list', 'task', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))
    models = {
        'ants.comment': {
            'Meta': {'object_name': 'comment'},
            'c_text': ('django.db.models.fields.TextField', [], {}),
            'c_time': ('django.db.models.fields.DateTimeField', [], {}),
            'cr_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ants.commentator']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'n_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ants.new']"}),
            'sent_indic': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'sw_id': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'tr_text': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        'ants.commentator': {
            'Meta': {'object_name': 'commentator'},
            'b_day': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True'}),
            'books': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'f_city': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True'}),
            'films': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'music': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'polit_conv': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'r_city': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True'}),
            'religion': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'study': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'sw_id': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'ants.new': {
            'Meta': {'object_name': 'new'},
            'coms': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'n_date': ('django.db.models.fields.DateTimeField', [], {}),
            'n_text': ('django.db.models.fields.TextField', [], {}),
            'sw_id': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'text_vector': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'tr_text': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        'ants.tag': {
            'Meta': {'object_name': 'tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'n_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ants.new']", 'null': 'True'}),
            'tg_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ants.tag_list']", 'null': 'True'})
        },
        'ants.tag_list': {
            'Meta': {'object_name': 'tag_list'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tg_text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'ants.task_list': {
            'Meta': {'object_name': 'task_list'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        'ants.thread_list': {
            'Meta': {'object_name': 'thread_list'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stat': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'task': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'w_type': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'work_done': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['ants']