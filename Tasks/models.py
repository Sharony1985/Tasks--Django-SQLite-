from django.db import models

# Create your models here.
class Task(models.Model):
    name_text = models.CharField(max_length=50)
    description_text =  models.CharField(max_length=200)
    task_date = models.DateTimeField('date of task')
    priority = models.IntegerField(default=0)


