from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tasks")

    class Meta:
        ordering = ("-created_at",)

    def __str(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name
