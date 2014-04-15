# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Prevention'
        db.create_table(u'edu_prevention', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('body', self.gf('tinymce.models.HTMLField')()),
        ))
        db.send_create_signal(u'edu', ['Prevention'])

        # Adding model 'Iso'
        db.create_table(u'edu_iso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('body', self.gf('tinymce.models.HTMLField')()),
        ))
        db.send_create_signal(u'edu', ['Iso'])

        # Adding M2M table for field ppe on 'Iso'
        m2m_table_name = db.shorten_name(u'edu_iso_ppe')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('iso', models.ForeignKey(orm[u'edu.iso'], null=False)),
            ('prevention', models.ForeignKey(orm[u'edu.prevention'], null=False))
        ))
        db.create_unique(m2m_table_name, ['iso_id', 'prevention_id'])

        # Adding model 'PathType'
        db.create_table(u'edu_pathtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('body', self.gf('tinymce.models.HTMLField')()),
        ))
        db.send_create_signal(u'edu', ['PathType'])

        # Adding model 'Pathogen'
        db.create_table(u'edu_pathogen', (
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sci_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('iso_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['edu.Iso'])),
            ('path_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['edu.PathType'])),
            ('body', self.gf('tinymce.models.HTMLField')()),
            ('symptom_body', self.gf('tinymce.models.HTMLField')()),
            ('reservoir_body', self.gf('tinymce.models.HTMLField')()),
        ))
        db.send_create_signal(u'edu', ['Pathogen'])

        # Adding model 'HAI'
        db.create_table(u'edu_hai', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('body', self.gf('tinymce.models.HTMLField')()),
            ('hai_def', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'edu', ['HAI'])

        # Adding M2M table for field path_type on 'HAI'
        m2m_table_name = db.shorten_name(u'edu_hai_path_type')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('hai', models.ForeignKey(orm[u'edu.hai'], null=False)),
            ('pathogen', models.ForeignKey(orm[u'edu.pathogen'], null=False))
        ))
        db.create_unique(m2m_table_name, ['hai_id', 'pathogen_id'])

        # Adding M2M table for field prev_tags on 'HAI'
        m2m_table_name = db.shorten_name(u'edu_hai_prev_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('hai', models.ForeignKey(orm[u'edu.hai'], null=False)),
            ('prevention', models.ForeignKey(orm[u'edu.prevention'], null=False))
        ))
        db.create_unique(m2m_table_name, ['hai_id', 'prevention_id'])

        # Adding model 'Article'
        db.create_table(u'edu_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('body', self.gf('tinymce.models.HTMLField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'edu', ['Article'])

        # Adding M2M table for field tags on 'Article'
        m2m_table_name = db.shorten_name(u'edu_article_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('article', models.ForeignKey(orm[u'edu.article'], null=False)),
            ('pathogen', models.ForeignKey(orm[u'edu.pathogen'], null=False))
        ))
        db.create_unique(m2m_table_name, ['article_id', 'pathogen_id'])

        # Adding M2M table for field iso_tags on 'Article'
        m2m_table_name = db.shorten_name(u'edu_article_iso_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('article', models.ForeignKey(orm[u'edu.article'], null=False)),
            ('iso', models.ForeignKey(orm[u'edu.iso'], null=False))
        ))
        db.create_unique(m2m_table_name, ['article_id', 'iso_id'])

        # Adding M2M table for field prev_tags on 'Article'
        m2m_table_name = db.shorten_name(u'edu_article_prev_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('article', models.ForeignKey(orm[u'edu.article'], null=False)),
            ('prevention', models.ForeignKey(orm[u'edu.prevention'], null=False))
        ))
        db.create_unique(m2m_table_name, ['article_id', 'prevention_id'])

        # Adding M2M table for field hai_tags on 'Article'
        m2m_table_name = db.shorten_name(u'edu_article_hai_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('article', models.ForeignKey(orm[u'edu.article'], null=False)),
            ('hai', models.ForeignKey(orm[u'edu.hai'], null=False))
        ))
        db.create_unique(m2m_table_name, ['article_id', 'hai_id'])


    def backwards(self, orm):
        # Deleting model 'Prevention'
        db.delete_table(u'edu_prevention')

        # Deleting model 'Iso'
        db.delete_table(u'edu_iso')

        # Removing M2M table for field ppe on 'Iso'
        db.delete_table(db.shorten_name(u'edu_iso_ppe'))

        # Deleting model 'PathType'
        db.delete_table(u'edu_pathtype')

        # Deleting model 'Pathogen'
        db.delete_table(u'edu_pathogen')

        # Deleting model 'HAI'
        db.delete_table(u'edu_hai')

        # Removing M2M table for field path_type on 'HAI'
        db.delete_table(db.shorten_name(u'edu_hai_path_type'))

        # Removing M2M table for field prev_tags on 'HAI'
        db.delete_table(db.shorten_name(u'edu_hai_prev_tags'))

        # Deleting model 'Article'
        db.delete_table(u'edu_article')

        # Removing M2M table for field tags on 'Article'
        db.delete_table(db.shorten_name(u'edu_article_tags'))

        # Removing M2M table for field iso_tags on 'Article'
        db.delete_table(db.shorten_name(u'edu_article_iso_tags'))

        # Removing M2M table for field prev_tags on 'Article'
        db.delete_table(db.shorten_name(u'edu_article_prev_tags'))

        # Removing M2M table for field hai_tags on 'Article'
        db.delete_table(db.shorten_name(u'edu_article_hai_tags'))


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
            'body': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ppe': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['edu.Prevention']", 'symmetrical': 'False'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'edu.pathogen': {
            'Meta': {'ordering': "['tag']", 'object_name': 'Pathogen'},
            'body': ('tinymce.models.HTMLField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['edu.Iso']"}),
            'path_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['edu.PathType']"}),
            'reservoir_body': ('tinymce.models.HTMLField', [], {}),
            'sci_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'symptom_body': ('tinymce.models.HTMLField', [], {}),
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
            'body': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['edu']