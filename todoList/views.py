from django.shortcuts import render, redirect
from .forms import listForm

from .models import List


# Create your views here.
def search_tasks(request):
    if request.method == 'GET':
        user_search = request.GET.get('search') or ''
        returned_item = List.objects.filter(task__icontains=user_search)
        context = {
            'tasks': returned_item
        }
        return render(request, 'index.html', context)


def task_view(request):
    tasks = List.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context)


def add_new_tasks(request):
    if request.method == 'POST':
        form = listForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_view')
    else:
        form = listForm()
    return render(request, 'add.html', {'form': form})


def update_list(request, id):
    task = List.objects.get(id=id)
    form = listForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('task_view')
    return render(request, 'update.html', {'form': form})


def delete_item(request, id):
    task = List.objects.get(id=id)
    task.delete()
    return redirect('task_view')
