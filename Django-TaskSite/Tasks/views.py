from django.shortcuts import render

# Create your views here.
from Tasks.models import Task

def index(request):
    task_list = Task.objects.all().order_by('priority')
    context = {'task_list': task_list}
    return render(request, 'Tasks/index.html', context)