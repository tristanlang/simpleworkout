from django.contrib import admin
from workout.models import Category, Equipment, MovementTag, Movement, Ownership, Preference, RequiredEquipment, User, Workout, Log

admin.site.register(Category)
admin.site.register(Equipment)
admin.site.register(Movement)
admin.site.register(MovementTag)
admin.site.register(Ownership)
admin.site.register(Preference)
admin.site.register(RequiredEquipment)
admin.site.register(User)
admin.site.register(Workout)
admin.site.register(Log)