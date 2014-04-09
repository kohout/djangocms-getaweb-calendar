# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Event.start_on'
        db.delete_column(u'djangocms_calendar_event', 'start_on')

        # Deleting field 'Event.end_on'
        db.delete_column(u'djangocms_calendar_event', 'end_on')

        # Adding field 'Event.start_date'
        db.add_column(u'djangocms_calendar_event', 'start_date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 4, 9, 0, 0)),
                      keep_default=False)

        # Adding field 'Event.start_time'
        db.add_column(u'djangocms_calendar_event', 'start_time',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Event.end_date'
        db.add_column(u'djangocms_calendar_event', 'end_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Event.end_time'
        db.add_column(u'djangocms_calendar_event', 'end_time',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Event.start_on'
        db.add_column(u'djangocms_calendar_event', 'start_on',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 4, 9, 0, 0)),
                      keep_default=False)

        # Adding field 'Event.end_on'
        db.add_column(u'djangocms_calendar_event', 'end_on',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Event.start_date'
        db.delete_column(u'djangocms_calendar_event', 'start_date')

        # Deleting field 'Event.start_time'
        db.delete_column(u'djangocms_calendar_event', 'start_time')

        # Deleting field 'Event.end_date'
        db.delete_column(u'djangocms_calendar_event', 'end_date')

        # Deleting field 'Event.end_time'
        db.delete_column(u'djangocms_calendar_event', 'end_time')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'djangocms_calendar.event': {
            'Meta': {'ordering': "('start_date', 'start_time')", 'object_name': 'Event'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['djangocms_calendar.EventCategory']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'start_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'djangocms_calendar.eventcalendarpluginmodel': {
            'Meta': {'object_name': 'EventCalendarPluginModel', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'selected_categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['djangocms_calendar.EventCategory']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'view_mode': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'djangocms_calendar.eventcategory': {
            'Meta': {'object_name': 'EventCategory'},
            'color': ('colors.fields.ColorField', [], {'default': "'FF0000'", 'max_length': '7'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['djangocms_calendar.EventCategory']", 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['djangocms_calendar']