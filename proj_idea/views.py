from django.http import Http404
from django.shortcuts import render
from .models import ProjIdea
def index(request):
    newest_proj = ProjIdea.objects.order_by('-mail-Id')[:15]
    context = {'newest_proj': newest_proj}
    return render(request, 'proj_idea/index.html', context)
def show(request, proj_idea_id):
    try:

        project = ProjIdea.objects.get(pk=proj_idea_id)
    except ProjIdea.DoesNotExist:
        raise Http404("Project does not exist")
    return render(request, 'proj_idea/show.html', {'project': project})    
