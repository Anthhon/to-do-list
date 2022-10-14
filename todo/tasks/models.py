from django.db import models

class Task(models.Model):
    '''
    STATUS é um tipo de valor personalizável, que pode ser atribuído a objetos, neste caso, está sendo utilizado para mostrar se uma tarefa já foi feita ou não
    '''
    STATUS = (
        ('Doing', 'Doing'),
        ('Done', 'Done')
    )
    '''
    Title = Cria um campo de título
    Description = Cria um campo de textos longos
    Done = Variável que define o status de uma tarefa usando o método 'Choices'

    created_at && update_at -> Boa prática de criação de logs para tarefas
    '''
    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(
        max_length=5,
        choices=STATUS,
    )
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    # Coloca o nome da tarefa como o próprio título na tela de administrador
    def __str__(self):
        return self.title