from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    related = models.ManyToManyField('self',blank=True,symmetrical=True)

    def __str__(self):
        return f"#{self.id}.{self.title}"     
    # todo:return status



class NotePointer(models.Model):
    # RELATION_TYPE_CHOICES = (
    #     ('include', 'Include'),
    #     ('tag', 'Tag'),
    # )
    # relation_type = models.CharField(max_length=20, choices=RELATION_TYPE_CHOICES)

    from_note = models.ForeignKey(Note, related_name='from_note', on_delete=models.CASCADE)
    to_note = models.ForeignKey(Note, related_name='to_note', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.from_note} -> {self.to_note}"
    
