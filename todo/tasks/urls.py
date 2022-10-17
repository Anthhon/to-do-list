from django.urls import path
from .views import taskList, taskView, newTask, editTask

'''
Esse arquivo sempre será chamado pelo 'todo/urls.py', e tem como função retornar a função TaskList que foi previamente importada no código acima
'''
urlpatterns = [
    path('', taskList, name='tasklist'),
    path('task/<int:id>', taskView, name='task-view'),
    path('newtask/', newTask, name='new-task'),
    path('editask/<int:id>', editTask, name= 'edit-task')
]
