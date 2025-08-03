from django.db import models

# Create your models here.
class blogModel(models.Model):
    title=models.CharField(max_length=20)
    decription=models.TextField()
    def __str__(self):
        return (f'{self.title}')

class praticeModel(models.Model):
    question=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    def __str__(self):
        return (f'{self.question}')