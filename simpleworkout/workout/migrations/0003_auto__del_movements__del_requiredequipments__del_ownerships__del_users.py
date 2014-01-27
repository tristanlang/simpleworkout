# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Movements'
        db.delete_table('workout_movements')

        # Deleting model 'RequiredEquipments'
        db.delete_table('workout_requiredequipments')

        # Deleting model 'Ownerships'
        db.delete_table('workout_ownerships')

        # Deleting model 'Users'
        db.delete_table('workout_users')

        # Deleting model 'Workouts'
        db.delete_table('workout_workouts')

        # Deleting model 'MovementTags'
        db.delete_table('workout_movementtags')

        # Deleting model 'Equipments'
        db.delete_table('workout_equipments')

        # Deleting model 'Categories'
        db.delete_table('workout_categories')

        # Deleting model 'Preferences'
        db.delete_table('workout_preferences')

        # Adding model 'MovementTag'
        db.create_table('workout_movementtag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('workout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Workout'])),
            ('movement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Movement'])),
        ))
        db.send_create_signal('workout', ['MovementTag'])

        # Adding model 'Ownership'
        db.create_table('workout_ownership', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.User'])),
            ('equipment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Equipment'])),
        ))
        db.send_create_signal('workout', ['Ownership'])

        # Adding model 'Log'
        db.create_table('workout_log', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.User'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('workout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Workout'])),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
        ))
        db.send_create_signal('workout', ['Log'])

        # Adding model 'User'
        db.create_table('workout_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('password_hash', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('workout', ['User'])

        # Adding model 'Workout'
        db.create_table('workout_workout', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Category'])),
            ('detail', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('workout', ['Workout'])

        # Adding model 'RequiredEquipment'
        db.create_table('workout_requiredequipment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('workout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Workout'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Equipment'])),
        ))
        db.send_create_signal('workout', ['RequiredEquipment'])

        # Adding model 'Movement'
        db.create_table('workout_movement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movement', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('workout', ['Movement'])

        # Adding model 'Category'
        db.create_table('workout_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('workout', ['Category'])

        # Adding model 'Preference'
        db.create_table('workout_preference', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.User'])),
            ('days_per_week', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=2)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Category'])),
        ))
        db.send_create_signal('workout', ['Preference'])

        # Adding model 'Equipment'
        db.create_table('workout_equipment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('workout', ['Equipment'])


    def backwards(self, orm):
        # Adding model 'Movements'
        db.create_table('workout_movements', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movement', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('workout', ['Movements'])

        # Adding model 'RequiredEquipments'
        db.create_table('workout_requiredequipments', (
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Equipments'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('workout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Workouts'])),
        ))
        db.send_create_signal('workout', ['RequiredEquipments'])

        # Adding model 'Ownerships'
        db.create_table('workout_ownerships', (
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Users'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('equipment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Equipments'])),
        ))
        db.send_create_signal('workout', ['Ownerships'])

        # Adding model 'Users'
        db.create_table('workout_users', (
            ('username', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password_hash', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('workout', ['Users'])

        # Adding model 'Workouts'
        db.create_table('workout_workouts', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('detail', self.gf('django.db.models.fields.TextField')()),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Categories'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('workout', ['Workouts'])

        # Adding model 'MovementTags'
        db.create_table('workout_movementtags', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Movements'])),
            ('workout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Workouts'])),
        ))
        db.send_create_signal('workout', ['MovementTags'])

        # Adding model 'Equipments'
        db.create_table('workout_equipments', (
            ('item', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('workout', ['Equipments'])

        # Adding model 'Categories'
        db.create_table('workout_categories', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('workout', ['Categories'])

        # Adding model 'Preferences'
        db.create_table('workout_preferences', (
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Users'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('days_per_week', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=2)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Categories'])),
        ))
        db.send_create_signal('workout', ['Preferences'])

        # Deleting model 'MovementTag'
        db.delete_table('workout_movementtag')

        # Deleting model 'Ownership'
        db.delete_table('workout_ownership')

        # Deleting model 'Log'
        db.delete_table('workout_log')

        # Deleting model 'User'
        db.delete_table('workout_user')

        # Deleting model 'Workout'
        db.delete_table('workout_workout')

        # Deleting model 'RequiredEquipment'
        db.delete_table('workout_requiredequipment')

        # Deleting model 'Movement'
        db.delete_table('workout_movement')

        # Deleting model 'Category'
        db.delete_table('workout_category')

        # Deleting model 'Preference'
        db.delete_table('workout_preference')

        # Deleting model 'Equipment'
        db.delete_table('workout_equipment')


    models = {
        'workout.category': {
            'Meta': {'object_name': 'Category'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'workout.equipment': {
            'Meta': {'object_name': 'Equipment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'workout.log': {
            'Meta': {'object_name': 'Log'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workout.User']"}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workout.Workout']"})
        },
        'workout.movement': {
            'Meta': {'object_name': 'Movement'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movement': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'workout.movementtag': {
            'Meta': {'object_name': 'MovementTag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movement': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workout.Movement']"}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workout.Workout']"})
        },
        'workout.ownership': {
            'Meta': {'object_name': 'Ownership'},
            'equipment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workout.Equipment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workout.User']"})
        },
        'workout.preference': {
            'Meta': {'object_name': 'Preference'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workout.Category']"}),
            'days_per_week': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workout.User']"})
        },
        'workout.requiredequipment': {
            'Meta': {'object_name': 'RequiredEquipment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workout.Equipment']"}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workout.Workout']"})
        },
        'workout.user': {
            'Meta': {'object_name': 'User'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password_hash': ('django.db.models.fields.TextField', [], {}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'workout.workout': {
            'Meta': {'object_name': 'Workout'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workout.Category']"}),
            'detail': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['workout']