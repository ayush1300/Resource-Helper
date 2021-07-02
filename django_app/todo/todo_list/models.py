from django.db import models

# Create your models here.


class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.item + ' | ' + str(self.completed)


class ComponentList(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE, null=True)
    topic = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    link = models.CharField(max_length=1000)

    def __str__(self):
        return self.topic
