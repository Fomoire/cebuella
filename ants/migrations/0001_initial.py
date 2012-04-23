# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'tag_list'
        db.create_table('ants_tag_list', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tg_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('ants', ['tag_list'])

        # Adding model 'new'
        db.create_table('ants_new', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('n_text', self.gf('django.db.models.fields.TextField')()),
            ('n_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('tr_text', self.gf('django.db.models.fields.TextField')(null=True)),
            ('sw_id', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('text_vector', self.gf('django.db.models.fields.TextField')(null=True)),
            ('coms', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('likes', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('ants', ['new'])

        # Adding model 'tag'
        db.create_table('ants_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tg_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ants.tag_list'])),
            ('n_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ants.new'])),
        ))
        db.send_create_signal('ants', ['tag'])

        # Adding model 'commentator'
        db.create_table('ants_commentator', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('b_day', self.gf('django.db.models.fields.CharField')(max_length=80, null=True)),
            ('r_city', self.gf('django.db.models.fields.CharField')(max_length=120, null=True)),
            ('f_city', self.gf('django.db.models.fields.CharField')(max_length=120, null=True)),
            ('study', self.gf('django.db.models.fields.TextField')(null=True)),
            ('music', self.gf('django.db.models.fields.TextField')(null=True)),
            ('books', self.gf('django.db.models.fields.TextField')(null=True)),
            ('religion', self.gf('django.db.models.fields.TextField')(null=True)),
            ('polit_conv', self.gf('django.db.models.fields.TextField')(null=True)),
            ('films', self.gf('django.db.models.fields.TextField')(null=True)),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=1, null=True)),
            ('sw_id', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal('ants', ['commentator'])

        # Adding model 'comment'
        db.create_table('ants_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cr_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ants.commentator'])),
            ('n_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ants.new'])),
            ('c_text', self.gf('django.db.models.fields.TextField')()),
            ('tr_text', self.gf('django.db.models.fields.TextField')(null=True)),
            ('sent_indic', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('sw_id', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('c_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('likes', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('ants', ['comment'])

        # Adding model 'down_site'
        db.create_table('ants_down_site', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('sw', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('ants', ['down_site'])

    def backwards(self, orm):
        # Deleting model 'tag_list'
        db.delete_table('ants_tag_list')

        # Deleting model 'new'
        db.delete_table('ants_new')

        # Deleting model 'tag'
        db.delete_table('ants_tag')

        # Deleting model 'commentator'
        db.delete_table('ants_commentator')

        # Deleting model 'comment'
        db.delete_table('ants_comment')

        # Deleting model 'down_site'
        db.delete_table('ants_down_site')

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
            'n_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'n_text': ('django.db.models.fields.TextField', [], {}),
            'sw_id': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'text_vector': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'tr_text': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        'ants.tag': {
            'Meta': {'object_name': 'tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'n_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ants.new']"}),
            'tg_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ants.tag_list']"})
        },
        'ants.tag_list': {
            'Meta': {'object_name': 'tag_list'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tg_text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['ants']