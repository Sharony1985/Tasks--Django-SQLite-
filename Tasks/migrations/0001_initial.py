# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Priority'
        db.create_table('Tasks_priority', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('priority_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('priority_value', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('Tasks', ['Priority'])

        # Adding model 'Task'
        db.create_table('Tasks_task', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_text', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('task_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('priority', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Tasks.Priority'])),
        ))
        db.send_create_signal('Tasks', ['Task'])


    def backwards(self, orm):
        # Deleting model 'Priority'
        db.delete_table('Tasks_priority')

        # Deleting model 'Task'
        db.delete_table('Tasks_task')


    models = {
        'Tasks.priority': {
            'Meta': {'object_name': 'Priority'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'priority_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'priority_value': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'Tasks.task': {
            'Meta': {'object_name': 'Task'},
            'description_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_text': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'priority': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Tasks.Priority']"}),
            'task_date': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['Tasks']