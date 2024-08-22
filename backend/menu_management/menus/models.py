# menus/models.py

from django.db import models
import uuid

class MenuItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    depth = models.PositiveIntegerField(default=0)  # to keep track of hierarchical level

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['depth', 'name']
