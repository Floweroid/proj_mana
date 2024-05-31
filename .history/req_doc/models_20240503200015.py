from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name='项目名称')
    description = models.TextField(verbose_name='项目描述')

    def __str__(self):
        return self.name


class Definition(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='definitions', verbose_name='所属项目')
    name = models.CharField(max_length=100, verbose_name='名称')
    description = models.TextField(verbose_name='描述')
    alias = models.CharField(max_length=100, blank=True, null=True, verbose_name='别名')

    def __str__(self):
        return self.name

class Requirement(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='requirements', verbose_name='所属项目',null=True)
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
    