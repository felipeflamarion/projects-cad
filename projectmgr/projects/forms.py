from django.forms import ModelForm
from projects.models import Activity, Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "initial_date",
            "final_date",
        ]


class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = [
            "name",
            "project_id",
            "initial_date",
            "final_date",
        ]
