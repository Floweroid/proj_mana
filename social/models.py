# act/models.py

from django.db import models
from django.utils import timezone
from note.models import Note
from datetime import date

class Todo(Note):
    start_time = models.DateTimeField(verbose_name='Start Time', null=True, blank=True)
    end_time = models.DateTimeField(verbose_name='End Time', null=True, blank=True)
    due = models.DateTimeField(verbose_name='Deadline', null=True, blank=True)
    
    def __str__(self):
        return f"#{self.id}.{self.title}"  # Changed from self.name to self.title
    
    def duration(self):
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        return None
    
class Person(Note):
    lName = models.CharField(max_length=100, verbose_name='Last Name')
    mid = models.CharField(max_length=100, verbose_name='Middle Name', null=True, blank=True)
    fName = models.CharField(max_length=100, verbose_name='First Name')
    birthdate = models.DateField(verbose_name='Birthdate', null=True, blank=True)

    # @property
    def age(self):
        if self.birthdate:
            today = date.today()
            return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return None
    
    def __str__(self):
        return f"{self.fName} {self.lName}"

class Media(models.Model):
    MEDIA_CHOICES = (
        ('Linkin','Linkin'),
        ('TelephoneNum','TelephoneNum'),
        ('Wechat', 'Wechat'),
        ('Facebook', 'Facebook'),
        ('Twitter', 'Twitter'),
        ('Instagram', 'Instagram'),
        # Add more media types as needed
    )
    
    person = models.ForeignKey(Person, related_name='media_accounts', on_delete=models.CASCADE, verbose_name='Person')
    media = models.CharField(max_length=50, choices=MEDIA_CHOICES, verbose_name='Media')
    account = models.CharField(max_length=100, verbose_name='Account')

    def __str__(self):
        return f"{self.person} - {self.media}: {self.account}"

class SocialRelationship(models.Model):
    relation = models.CharField(max_length=10, verbose_name='Relationship')
    from_person = models.ForeignKey(Person, related_name='from_relationships', on_delete=models.CASCADE, verbose_name='From Person')
    to_person = models.ForeignKey(Person, related_name='to_relationships', on_delete=models.CASCADE, verbose_name='To Person')

    def __str__(self):
        return f"{self.from_person} -> {self.to_person}: {self.relation}"