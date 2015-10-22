from django.contrib import admin

from .models import Exercise, Program, RepetitionSet, Routine, RoutineStep


class ExerciseAdmin(admin.ModelAdmin):
    fields = ["name", "movement_type"]


class RoutineAdmin(admin.ModelAdmin):
    fields = ["name", "routine_step"]


class ProgramAdmin(admin.ModelAdmin):
    fields = ["name", "routine", "day_spread"]


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Routine, RoutineAdmin)
admin.site.register(RepetitionSet)
admin.site.register(RoutineStep)
