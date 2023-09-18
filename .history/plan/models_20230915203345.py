from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
class Member(models.Model):
    name = models.CharField(max_length=20)
    tasks = models.ManyToManyField(Task, through="Assignment")

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Member, through="Assignment")
    
    def __str__(self):
        return self.name
    
class Assignment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
