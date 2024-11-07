from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render

from apps.abouts.models import About


@permission_required("Abouts watching")
def about(request):
    """
    this about function
    there context use for html, it got all obj
    """

    # About.objects.all().delete()
    context = {
               'abouts': About.objects.all(),
    }
    return render(request=request, template_name='about.html', context=context)
