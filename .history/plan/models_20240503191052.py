from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text

class Member(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Task(models.Model):
    # Define choices for the task status
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('InProgress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=128)
    description = models.TextField(max_length=440)
    members = models.ManyToManyField(Member, through="Assignment")
    create_time = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def get_members_display(self):
        return ", ".join([str(member) for member in self.members.all()])

    get_members_display.short_description = 'Assign to'  # Optional, sets the column name in the admin list view

    def __str__(self):
        return self.title

class Assignment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

class Book(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    
    def __str__(self):
        return self.name
    
    def get_books_display(self):
        return ", ".join([str(book) for book in self.books.all()])
    get_books_display.short_description = 'Books'  # Optional, sets the column name in the admin list view

class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name='项目名称')
    description = models.TextField(verbose_name='项目描述')

    def __str__(self):
        return self.name


class Definition(models.Model):
    name = models.CharField(max_length=100, verbose_name='名称')
    description = models.TextField(verbose_name='描述')

    def __str__(self):
        return self.name

class Requirement(models.Model):
    STATUS_CHOICES = (
        ('已完成', '已完成'),
        ('进行中', '进行中'),
        ('未开始', '未开始'),
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name='状态')
    description = models.TextField(verbose_name='描述')
    definitions = models.ManyToManyField(Definition, verbose_name='相关定义', related_name='requirements')
    priority = models.IntegerField(verbose_name='优先级')
    
    def __str__(self):
        return f"Requirement {self.id}: {self.description}"
    
