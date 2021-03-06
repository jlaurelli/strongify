from django.contrib import admin

from .models import Exercise, Program, RepetitionSet, Routine, RoutineStep


class ExerciseAdmin(admin.ModelAdmin):
    fields = ["name", "movement_type"]


class RepetitionSetAdmin(admin.ModelAdmin):
    ordering = ("repetition_set",)


class RoutineAdmin(admin.ModelAdmin):
    ordering = ("name",)
    fields = ["program", "name"]


class RoutineStepInline(admin.StackedInline):
    model = RoutineStep


class RoutineInline(admin.StackedInline):
    model = Routine


class ProgramAdmin(admin.ModelAdmin):
    fields = ["day_spread", "name"]
    inlines = [RoutineInline]


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(RepetitionSet, RepetitionSetAdmin)
admin.site.register(Routine, RoutineAdmin)
admin.site.register(RoutineStep)
