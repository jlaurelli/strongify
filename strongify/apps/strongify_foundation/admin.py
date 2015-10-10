from django.contrib import admin

from .models import Exercise, Program, Routine


class ExerciseAdmin(admin.ModelAdmin):
    fields = ["name"]


class RoutineAdmin(admin.ModelAdmin):
    fields = ["name", "exercise"]


class ProgramAdmin(admin.ModelAdmin):
    fields = ["name", "routine"]


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Routine, RoutineAdmin)
