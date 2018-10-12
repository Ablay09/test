from django.db import models


class Task_list(models.Model):
    name = models.CharField(max_length=255)
    time = models.DateTimeField('Created time of list is', auto_now_add=False)

    def __str__(self):
        return self.name


class Task(models.Model):
    task_list = models.ForeignKey(Task_list, on_delete=models.CASCADE, null=True)
    task_name = models.CharField(max_length=255)
    created_date = models.DateTimeField('Created date', auto_now_add=False)
    finished_date = models.DateTimeField('Finished date', auto_now_add=False)
    ADMIN = 'ADMIN'
    USER = 'USER'
    GUEST = 'GUEST'
    OWNER_CHOICES = (
        (ADMIN, 'Admin'),
        (USER,  'User'),
        (GUEST, 'Guest')
    )
    owner = models.CharField(max_length=250, choices=OWNER_CHOICES, default=ADMIN)
    mark = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name
