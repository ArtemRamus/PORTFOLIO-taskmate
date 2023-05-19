from django.db import models
from django.contrib.auth.models import User

class TaskList(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    
    class Meta:
        ordering=['id']
    
    def __str__(self):
        if self.done:
            task_status = "done"
        else:
            task_status = "pending"
        return f"{self.task}, {task_status}, {str(self.owner)}"