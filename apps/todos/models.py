from django.db import models

class ToDo(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='title'
    )

    task = models.TextField(
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='created at:'
    )

    completed = models.BooleanField(
        default=False,
    )


    def __str__(self):
        return self.title