# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EventCalendarPluginModel'
        db.create_table(u'djangocms_calendar_eventcalendarpluginmodel', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('view_mode', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'djangocms_calendar', ['EventCalendarPluginModel'])

        # Adding M2M table for field selected_categories on 'EventCalendarPluginModel'
        m2m_table_name = db.shorten_name(u'djangocms_calendar_eventcalendarpluginmodel_selected_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('eventcalendarpluginmodel', models.ForeignKey(orm[u'djangocms_calendar.eventcalendarpluginmodel'], null=False)),
            ('eventcategory', models.ForeignKey(orm[u'djangocms_calendar.eventcategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['eventcalendarpluginmodel_id', 'eventcategory_id'])

        # Adding model 'EventCategory'
        db.create_table(u'djangocms_calendar_eventcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['djangocms_calendar.EventCategory'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('color', self.gf('colors.fields.ColorField')(default='FF0000', max_length=7)),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'djangocms_calendar', ['EventCategory'])

        # Adding model 'Event'
        db.create_table(u'djangocms_calendar_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['djangocms_calendar.EventCategory'], null=True, blank=True)),
        ))
        db.send_create_signal(u'djangocms_calendar', ['Event'])


    def backwards(self, orm):
        # Deleting model 'EventCalendarPluginModel'
        db.delete_table(u'djangocms_calendar_eventcalendarpluginmodel')

        # Removing M2M table for field selected_categories on 'EventCalendarPluginModel'
        db.delete_table(db.shorten_name(u'djangocms_calendar_eventcalendarpluginmodel_selected_categories'))

        # Deleting model 'EventCategory'
        db.delete_table(u'djangocms_calendar_eventcategory')

        # Deleting model 'Event'
        db.delete_table(u'djangocms_calendar_event')


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
            'Meta': {'ordering': "('start_on',)", 'object_name': 'Event'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['djangocms_calendar.EventCategory']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_on': ('django.db.models.fields.DateTimeField', [], {}),
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['djangocms_calendar.EventCategory']", 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['djangocms_calendar']