from django.urls import path
from .views import TaskList, taskView

'''
Esse arquivo sempre será chamado pelo 'todo/urls.py', e tem como função retornar a função TaskList que foi previamente importada no código acima
'''
urlpatterns = [
    path('', TaskList, name='tasklist'),

    path('task/<int:id>', taskView, name='your-name'),
]
