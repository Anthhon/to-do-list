from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Task

'''
    A função 'TaskList' tem um nome puramente ilustrativo, e guarda o endereço da página HTML que deve ser retornada.

    A variável 'tasks' possui a tarefa de guardar todos os objetos advindos do model 'Task', para que sejam retornados ao usuário
'''
def TaskList(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

'''
A função 'taskView' tem como função, retornar ao usuário informações mais detalhadas sobre alguma task.

Importando a função "get_object_or_404 é possível retornar valores de objetos usando uma ID específica ou retornar uma tela de erro caso não seja encontrado a task

Get_object_or_404 arguments -> Modelo que está será usado, e uma primary key que será usada para identificar qual dos modelos criados deve ser utilizado
'''
def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks.html', {'tasks': task})