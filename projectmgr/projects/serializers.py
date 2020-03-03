from rest_framework import serializers
from projects.models import Activity, Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name", "initial_date", "final_date"]


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = [
            "id",
            "project_id",
            "name",
            "initial_date",
            "final_date","is_finished"
        ]