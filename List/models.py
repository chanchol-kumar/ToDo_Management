from django.db import models

class ToDoModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    status = models.BooleanField(default=False)
        
    def __str__(self):
            return self.title