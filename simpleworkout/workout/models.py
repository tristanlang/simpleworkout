from django.db import models

class Categories(models.Model):
    category = models.CharField(max_length=20)

class Movements(models.Model):
    movement = models.CharField(max_length=100)

class Workouts(models.Model):
    date = models.DateTimeField('date of workout')
    category = models.ForeignKey(Categories)
    detail = models.TextField()
    notes = models.CharField(max_length=200, null=True)

class Equipments(models.Model):
    item = models.CharField(max_length=100)

class Users(models.Model):
    username = models.CharField(max_length=20)
    password_hash = models.TextField()

class Preferences(models.Model):
    user = models.ForeignKey(Users)
    days_per_week = models.PositiveSmallIntegerField(default=2)
    category = models.ForeignKey(Categories)

class Ownerships(models.Model):
    user = models.ForeignKey(Users)
    equipment = models.ForeignKey(Equipments)

class MovementTags(models.Model):
    workout = models.ForeignKey(Workouts)
    movement = models.ForeignKey(Movements)

class RequiredEquipments(models.Model):
    workout = models.ForeignKey(Workouts)
    item = models.ForeignKey(Equipments)