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
    # tasks = models.ManyToManyField(Task, through="Assignment")

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=440)
    members = models.ManyToManyField(Member, through="Assignment")
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    
    def get_books_display(self):
        return ", ".join([str(member) for member in self.members.all()])
    
    def __str__(self):
        return self.title
    
class Assignment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)



class Book(models.Model):
    title = models.CharField(max_length=100)
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    def get_books_display(self):
        return ", ".join([str(book) for book in self.books.all()])
    get_books_display.short_description = 'Books'  # Optional, sets the column name in the admin list view