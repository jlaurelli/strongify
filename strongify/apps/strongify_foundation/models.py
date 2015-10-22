import uuid
import django.contrib.postgres.fields as pgfields
from django.db import models

"""
Program - A set of routines. This encompasses several days worth of workouts
          and together form a complete routine.

          Programs can have multiple "phases" (basically a subprogram).

Routine - A set of exercises that compose a unit in a program. Acts as a
          linker between the programs and exercises.

RoutineStep - A sub-component of the Routine, it acts as a linker between
              exercises and routines.

Exercise - An atomic exercise movement. These are independent of a routine or
           program, and multiples can exist within any routine/program.

TODO - Figure out how to set weights and design workout attempt models.
"""


class Program(models.Model):
    DAY_SPREADS = [
        (0, "other"),
        (1, "1 Day"),
        (2, "2 Days"),
        (3, "3 Days"),
        (4, "4 Days"),
        (5, "5 Days"),
        (6, "6 Days"),
        (7, "Everyday")
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    day_spread = models.PositiveIntegerField(choices=DAY_SPREADS, default=3)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class RepetitionSet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    repetition_set = pgfields.ArrayField(
        models.PositiveIntegerField(),
        size=2
    )

    def __str__(self):
        return "{} X {}".format(self.repetition_set[0], self.repetition_set[1])


class Routine(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    program = models.ForeignKey("Program")

    def __str__(self):
        return self.name

    class Meta:
        unique_together = (("program", "name"),)


class RoutineStep(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    exercise = models.ForeignKey("Exercise")
    repetition_set = models.ForeignKey("RepetitionSet")
    routine = models.ManyToManyField("Routine")

    def __str__(self):
        return "{} ({})".format(self.exercise, self.repetition_set)

    class Meta:
        unique_together = (("repetition_set", "exercise"),)


class Exercise(models.Model):
    MOVEMENT_TYPES = [
        ("compound", "Compound"),
        ("isolation", "Isolation")
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    movement_type = models.CharField(max_length=100, choices=MOVEMENT_TYPES,
                                     default="compound")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
