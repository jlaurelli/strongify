from django.contrib import admin

from .models import Exercise, Program, Routine


class ExerciseAdmin(admin.ModelAdmin):
    fields = ["name", "movement_type"]


class RoutineAdmin(admin.ModelAdmin):
    fields = ["name", "exercise"]


class ProgramAdmin(admin.ModelAdmin):
    fields = ["name", "routine", "day_spread"]


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Routine, RoutineAdmin)
