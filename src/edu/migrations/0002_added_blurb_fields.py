# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Iso.blurb'
        db.add_column(u'edu_iso', 'blurb',
                      self.gf('tinymce.models.HTMLField')(default='placeholder'),
                      keep_default=False)

        # Adding field 'Prevention.blurb'
        db.add_column(u'edu_prevention', 'blurb',
                      self.gf('tinymce.models.HTMLField')(default='placeholder'),
                      keep_default=False)

        # Deleting field 'Pathogen.reservoir_body'
        db.delete_column(u'edu_pathogen', 'reservoir_body')

        # Deleting field 'Pathogen.symptom_body'
        db.delete_column(u'edu_pathogen', 'symptom_body')

        # Adding field 'Pathogen.blurb'
        db.add_column(u'edu_pathogen', 'blurb',
                      self.gf('tinymce.models.HTMLField')(default='placeholder'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Iso.blurb'
        db.delete_column(u'edu_iso', 'blurb')

        # Deleting field 'Prevention.blurb'
        db.delete_column(u'edu_prevention', 'blurb')

        # Adding field 'Pathogen.reservoir_body'
        db.add_column(u'edu_pathogen', 'reservoir_body',
                      self.gf('tinymce.models.HTMLField')(default='0'),
                      keep_default=False)

        # Adding field 'Pathogen.symptom_body'
        db.add_column(u'edu_pathogen', 'symptom_body',
                      self.gf('tinymce.models.HTMLField')(default='0'),
                      keep_default=False)

        # Deleting field 'Pathogen.blurb'
        db.delete_column(u'edu_pathogen', 'blurb')


    models = {
        u'edu.article': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Article'},
            'body': ('tinymce.models.HTMLField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'hai_tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['edu.HAI']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso_tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['edu.Iso']", 'symmetrical': 'False'}),
            'prev_tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['edu.Prevention']", 'symmetrical': 'False'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['edu.Pathogen']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'edu.hai': {
            'Meta': {'object_name': 'HAI'},
            'body': ('tinymce.models.HTMLField', [], {}),
            'hai_def': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path_type': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['edu.Pathogen']", 'symmetrical': 'False'}),
            'prev_tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['edu.Prevention']", 'symmetrical': 'False'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'edu.iso': {
            'Meta': {'object_name': 'Iso'},
            'blurb': ('tinymce.models.HTMLField', [], {}),
            'body': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ppe': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['edu.Prevention']", 'symmetrical': 'False'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'edu.pathogen': {
            'Meta': {'ordering': "['tag']", 'object_name': 'Pathogen'},
            'blurb': ('tinymce.models.HTMLField', [], {}),
            'body': ('tinymce.models.HTMLField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['edu.Iso']"}),
            'path_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['edu.PathType']"}),
            'sci_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'edu.pathtype': {
            'Meta': {'object_name': 'PathType'},
            'body': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'edu.prevention': {
            'Meta': {'object_name': 'Prevention'},
            'blurb': ('tinymce.models.HTMLField', [], {}),
            'body': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['edu']