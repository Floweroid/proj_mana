from django.db import models

class Requirement(models.Model):
    name = models.CharField(max_length=100, verbose_name='名称')
    STATUS_CHOICES = (
        ('已取消', '已取消'),
        ('已完成', '已完成'),
        ('进行中', '进行中'),
        ('未开始', '未开始'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name='状态', default='未开始')
    description = models.TextField(verbose_name='描述', null=True)
    priority = models.IntegerField(verbose_name='优先级', default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='sub_requirements', on_delete=models.CASCADE, verbose_name='父需求')

    def __str__(self):
        return f"Requirement {self.id}: {self.description}"


class Note(models.Model):
    name = models.CharField(max_length=100, verbose_name='笔记名称')
    description = models.TextField(verbose_name='笔记',null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.name

