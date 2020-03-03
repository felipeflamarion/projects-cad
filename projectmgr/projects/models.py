from django.db import models


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    initial_date = models.DateField()
    final_date = models.DateField()


class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=30)
    initial_date = models.DateField()
    final_date = models.DateField()
    is_finished = models.BooleanField(
        null=True,
        blank=True,
        default=False
    )