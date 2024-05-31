from django.db import models
from act.models import Todo

class Person(models.Model):
    lName = models.CharField(max_length=100, verbose_name='Last Name')
    mid = models.CharField(max_length=100, verbose_name='Middle Name', null=True, blank=True)
    fName = models.CharField(max_length=100, verbose_name='First Name')
    hometown = models.CharField(max_length=100, verbose_name='Hometown', null=True, blank=True)
    description = models.TextField(verbose_name='Description', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    def __str__(self):
        return f"{self.fName} {self.lName}"

class SocialRelationship(models.Model):
    relation = models.CharField(max_length=10, verbose_name='Relationship')
    from_person = models.ForeignKey(Person, related_name='from_relationships', on_delete=models.CASCADE, verbose_name='From Person')
    to_person = models.ForeignKey(Person, related_name='to_relationships', on_delete=models.CASCADE, verbose_name='To Person')

    def __str__(self):
        return f"{self.from_person} -> {self.to_person}: {self.relation}"

class TodoPersonRelation(models.Model):
    person = models.ForeignKey('person', on_delete=models.CASCADE, verbose_name='Person')
    todo = models.ForeignKey('Todo', on_delete=models.CASCADE, verbose_name='Todo')
    
    def __str__(self):
        return f"Todo: {self.todo_id}, Event: {self.event_id}"
