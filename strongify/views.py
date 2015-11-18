from django.shortcuts import render

import strongify.apps.strongify_foundation.models as models

def home(request):
    return render(request, "index.html", {})

def program(request):
    programs = models.Program.objects.order_by("name")
    context = {"programs": programs}
    return render(request, "programs.html", context)
