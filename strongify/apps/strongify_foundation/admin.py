from django.contrib import admin

from .models import Exercise, Program, RepetitionSet, Routine, RoutineStep


class ExerciseAdmin(admin.ModelAdmin):
    fields = ["name", "movement_type"]


class RoutineStepInline(admin.StackedInline):
    model = RoutineStep
    extra = 3


class RoutineAdmin(admin.ModelAdmin):
    fields = ["name"]
    # inlines = [RoutineStepInline]


class RoutineInline(admin.StackedInline):
    model = Routine
    extra = 2


class ProgramAdmin(admin.ModelAdmin):
    fields = ["day_spread", "name"]
    inlines = [RoutineInline]


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Program, ProgramAdmin)
# admin.site.register(Routine, RoutineAdmin)
admin.site.register(RepetitionSet)
# admin.site.register(RoutineStep)
