from django import forms
from django import forms
from .models import Task


'''
A classe 'TaskForm' é apenas um espelho das informações que foram colocadas dentro
do modelo base 'Task', que será utilizada para exibir ao usuário apenas as informações
que forem julgadas necessárias.

No caso, as informações escolhidas para serem preenchidas pelo usuário, foram os campos
'tile' e 'description'
'''
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description')