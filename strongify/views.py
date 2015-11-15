from django.shortcuts import render

import strongify.apps.strongify_foundation.models as models

def home(request):
    programs = models.Program.objects.order_by("name")
    context = {"programs": programs}
    return render(request, "index.html", context)
