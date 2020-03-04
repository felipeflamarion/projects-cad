# coding: utf-8

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from projects.models import Activity, Project
from projects.forms import ActivityForm, ProjectForm


class ProjectsView(View):

    def get(self, request):
        context_dict = {
            "projects": Project.objects.all(),
            "form": ProjectForm(),
        }
        return render(request, 'projects/list.html', context_dict)
    
    def post(self, request):
        context_dict = {}
        
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/api/projects?registerSuccess=true')
        return self.get(request)


class ProjectView(View):

    def get(self, request, id):
        context_dict = {
            "project": Project.objects.get(pk=id),
            "activities": Activity.objects.filter(project_id=id),
            "form": ActivityForm(),
        }
        return render(request, 'projects/details.html', context_dict)

class ActivitiesView(View):

    def post(self, request, project_id: int):
        context_dict = {}
        
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                '/api/projects/%d?registerSuccess=true' %(project_id)
            )
        return render(request, 'projects/details.html', context_dict)

class ActivityView(View):

    def put(self, request, project_id: int, id: int):
        context_dict = {}
        return render(request, 'projects/details.html', context_dict)
