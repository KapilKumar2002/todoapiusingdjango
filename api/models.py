from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    isDone = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add= True)

    def __str__(self) -> str:
        return self.title