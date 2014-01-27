# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Users'
        db.create_table('workout_users', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('password_hash', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('workout', ['Users'])

        # Adding model 'Movements'
        db.create_table('workout_movements', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movement', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('workout', ['Movements'])

        # Adding model 'Ownerships'
        db.create_table('workout_ownerships', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Users'])),
            ('equipment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Equipments'])),
        ))
        db.send_create_signal('workout', ['Ownerships'])

        # Adding model 'Categories'
        db.create_table('workout_categories', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('workout', ['Categories'])

        # Adding model 'Preferences'
        db.create_table('workout_preferences', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Users'])),
            ('days_per_week', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=2)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Categories'])),
        ))
        db.send_create_signal('workout', ['Preferences'])

        # Adding model 'Workouts'
        db.create_table('workout_workouts', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Categories'])),
            ('detail', self.gf('django.db.models.fields.TextField')()),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
        ))
        db.send_create_signal('workout', ['Workouts'])

        # Adding model 'Equipments'
        db.create_table('workout_equipments', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('workout', ['Equipments'])

        # Adding model 'MovementTags'
        db.create_table('workout_movementtags', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('workout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Workouts'])),
            ('movement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Movements'])),
        ))
        db.send_create_signal('workout', ['MovementTags'])

        # Adding model 'RequiredEquipments'
        db.create_table('workout_requiredequipments', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('workout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Workouts'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Equipments'])),
        ))
        db.send_create_signal('workout', ['RequiredEquipments'])


    def backwards(self, orm):
        # Deleting model 'Users'
        db.delete_table('workout_users')

        # Deleting model 'Movements'
        db.delete_table('workout_movements')

        # Deleting model 'Ownerships'
        db.delete_table('workout_ownerships')

        # Deleting model 'Categories'
        db.delete_table('workout_categories')

        # Deleting model 'Preferences'
        db.delete_table('workout_preferences')

        # Deleting model 'Workouts'
        db.delete_table('workout_workouts')

        # Deleting model 'Equipments'
        db.delete_table('workout_equipments')

        # Deleting model 'MovementTags'
        db.delete_table('workout_movementtags')

        # Deleting model 'RequiredEquipments'
        db.delete_table('workout_requiredequipments')


    models = {
        'workout.categories': {
            'Meta': {'object_name': 'Categories'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'workout.equipments': {
            'Meta': {'object_name': 'Equipments'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'workout.movements': {
            'Meta': {'object_name': 'Movements'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movement': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'workout.movementtags': {
            'Meta': {'object_name': 'MovementTags'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movement': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workout.Movements']"}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workout.Workouts']"})
        },
        'workout.ownerships': {
            'Meta': {'object_name': 'Ownerships'},
            'equipment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workout.Equipments']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workout.Users']"})
        },
        'workout.preferences': {
            'Meta': {'object_name': 'Preferences'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workout.Categories']"}),
            'days_per_week': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workout.Users']"})
        },
        'workout.requiredequipments': {
            'Meta': {'object_name': 'RequiredEquipments'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workout.Equipments']"}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workout.Workouts']"})
        },
        'workout.users': {
            'Meta': {'object_name': 'Users'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password_hash': ('django.db.models.fields.TextField', [], {}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'workout.workouts': {
            'Meta': {'object_name': 'Workouts'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workout.Categories']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'detail': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'})
        }
    }

    complete_apps = ['workout']