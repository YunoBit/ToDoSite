from django.shortcuts import render , redirect
from django.db.models import Q

from apps.todos.models import ToDo


def homepage(request):
    if 'key_word' in request.GET:
        key = request.GET.get('words')
        todos = ToDo.objects.filter(Q(title__icontains=key) | Q(task=key))
    else:
        todos = ToDo.objects.all()
    return render(request, 'index.html', locals())

def create(request):
    if request.method == 'POST':
        name = request.POST['title']
        text = request.POST['task']
        todos = ToDo.objects.create(title = name , task = text)
        return redirect('index')
    return render(request, 'create.html')



def retrieve(request,pk):
    todos = ToDo.objects.get(id=pk)
    return render(request, 'detail.html', locals())


def update(request, pk):
    if request.method == "POST":
        name = request.POST['title']
        text = request.POST['task']
        todos = ToDo.objects.get(id = pk)
        todos.title = name
        todos.task = text
        todos.save()
        return redirect('detail', todos.id)
    return render(request, 'update.html', locals())


def distroy(request, pk):
    if request.method == 'POST':
        todos = ToDo.objects.get(id = pk)
        todos.delete()
        return redirect('index')
    return render (request, 'distroy.html', locals())



def done_tasks(request):
    completed_todos = ToDo.objects.filter(completed=True) 
    return render(request, 'done_tasks.html', {'completed_todos': completed_todos})


def done_tasks_add(request, pk):
    todo = ToDo.objects.get(id=pk)
    if todo.completed:
        todo.completed = False
        todo.save()
    else:
        todo.completed = True
        todo.save()
    return redirect('/')


