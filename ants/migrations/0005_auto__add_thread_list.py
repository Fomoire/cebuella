# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'thread_list'
        db.create_table('ants_thread_list', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stat', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('work_done', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('task', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('w_type', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('ants', ['thread_list'])

    def backwards(self, orm):
        # Deleting model 'thread_list'
        db.delete_table('ants_thread_list')

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
        'ants.down_site': {
            'Meta': {'object_name': 'down_site'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'sw': ('django.db.models.fields.CharField', [], {'max_length': '3'})
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
        'ants.thread_list': {
            'Meta': {'object_name': 'thread_list'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stat': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'task': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'w_type': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'work_done': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['ants']