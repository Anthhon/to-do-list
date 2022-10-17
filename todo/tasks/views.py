from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Task
from .forms import TaskForm

'''
    A função 'TaskList' tem um nome puramente ilustrativo, e guarda o endereço da página HTML que deve ser retornada.

    A variável 'tasks' possui a tarefa de guardar todos os objetos advindos do model 'Task', para que sejam retornados ao usuário
'''
def taskList(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'tasks': tasks})

'''
A função 'taskView' tem como função, retornar ao usuário informações mais detalhadas sobre alguma task.

Importando a função "get_object_or_404 é possível retornar valores de objetos usando uma ID específica ou retornar uma tela de erro caso não seja encontrado a task

Get_object_or_404 arguments -> Modelo que está será usado, e uma primary key que será usada para identificar qual dos modelos criados deve ser utilizado
'''
def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'task.html', {'task': task})


'''
A função 'newTask' tem como função a criação de tarefas usando uma interface dentro da própria aplicação

Primeiro é criado uma variável chamada 'form' que vai corresponder ao modelo do formulário e as suas devídas informações,
que podem ser vistas com mais detalhes no arquivo 'forms.py' que foi criado dentro da aplicação 'tasks'.

Se o site estiver fazendo uma requisição utilizando o método 'POST' será criado uma variável 'form' com as informações colocadas
previamente no formulário pelo usuário, e em seguida será feita uma verificação no formulário que caso seja válio, irá acionar uma sequência de ações onde
será criada a variável 'task' com as informações a serem salvas no formulário e será definido de maneira automática o estado do campo 'DONE" da tarefa como 'Doing',
em seguida a task criada será salva e o usuário será redirecionado para a página principal 
'''
def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'Doing'
            task.save()
            return redirect('/')

    else:
        form = TaskForm()
        return render(request, 'newtask.html', {'form': form})

def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if (request.method == 'POST'):
        form  = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task.save()
            return redirect('/')
        else:
            return render(request, 'editask.html', {'form': form, 'task': task})
    else:
        return render(request, 'editask.html', {'form': form, 'task': task})

def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return redirect('/')