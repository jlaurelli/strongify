import uuid
from django.db import models

"""
Program - A set of routines. This encompasses several days worth of workouts
          and together form a complete routine.

          Programs can have multiple "phases" (basically a subprogram).

Routine - A set of exercises that compose a unit in a program. Acts as a
          linker between the programs and exercises.

Exercise - An atomic exercise movement. These are independent of a routine or
           program, and multiples can exist within any routine/program.
"""


class Program(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    routine = models.ForeignKey(Routine)

    def __str__(self):
        return self.name


class Routine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    program = models.ForeignKey(Model)
    exercise = models.ForeignKey(Exercise)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
