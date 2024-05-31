from django.db import models

# Create your models here.

class Requirement(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='requirements', verbose_name='所属项目',null=True)
    STATUS_CHOICES = (
        ('已取消', '已取消'),
        ('已完成', '已完成'),
        ('进行中', '进行中'),
        ('未开始', '未开始'),
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name='状态', default='未开始')
    description = models.TextField(verbose_name='描述')
    priority = models.IntegerField(verbose_name='优先级',default=0)
    
    def __str__(self):
        return f"Requirement {self.id}: {self.description}"
    
class Note(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='notes', verbose_name='所属项目',null=True)
    name = models.CharField(max_length=100, verbose_name='笔记名称')
    description = models.TextField(verbose_name='笔记')

    def __str__(self):
        return self.name


class Act(models.Model):
    name = models.CharField(max_length=100, verbose_name='名称')
    description = models.TextField(verbose_name='解释')