from django.db import models

class WorkoutCategories(models.Model):
    category = models.CharField(max_length=20)

class Workouts(models.Model):
    date = models.DateTimeField('date of workout')
    category = models.ForeignKey(WorkoutCategories)
    detail = models.TextField()
    notes = models.CharField(max_length=200)

class Equipment(models.Model):
    item = models.CharField(max_length=100)

class Users(models.Model):
    username = models.CharField(max_length=20)
    password_hash = models.TextField()

class Preferences(models.Model):
    user = models.ForeignKey(Users)
    days_per_week = models.PositiveSmallIntegerField()
    category = models.ForeignKey(WorkoutCategories)

class Ownership(models.Model)
    user = models.ForeignKey(Users)
    equipment = models.ForeignKey(Equipment)