from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=20)
    def __str__(self):
        return self.category

class Movement(models.Model):
    movement = models.CharField(max_length=100)
    def __str__(self):
        return self.movement

class Workout(models.Model):
    category = models.ForeignKey(Category)
    detail = models.TextField()
    def __str__(self):
        return self.detail

class User(models.Model):
    username = models.CharField(max_length=20)
    password_hash = models.TextField()
    def __str__(self):
        return self.username

class Log(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField('date of workout')
    workout = models.ForeignKey(Workout)
    notes = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.date
    
class Equipment(models.Model):
    item = models.CharField(max_length=100)
    def __str__(self):
        return self.item

class Preference(models.Model):
    user = models.ForeignKey(User)
    days_per_week = models.PositiveSmallIntegerField(default=2)
    category = models.ForeignKey(Category)

class Ownership(models.Model):
    user = models.ForeignKey(User)
    equipment = models.ForeignKey(Equipment)

class MovementTag(models.Model):
    workout = models.ForeignKey(Workout)
    movement = models.ForeignKey(Movement)

class RequiredEquipment(models.Model):
    workout = models.ForeignKey(Workout)
    item = models.ForeignKey(Equipment)