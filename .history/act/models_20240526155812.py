

from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=100, verbose_name='名称')
    STATUS_CHOICES = (
        ('常态化', '常态化'),
        ('已取消', '已取消'),
        ('已完成', '已完成'),
        ('进行中', '进行中'),
        ('未开始', '未开始'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name='状态', default='未开始')
    description = models.TextField(verbose_name='描述', null=True,blank=True)
    priority = models.IntegerField(verbose_name='优先级', default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    # parents = models.ManyToManyField('self', through='TodoRelationship', symmetrical=False, verbose_name='父需求')

    start_time = models.DateTimeField(verbose_name='开始时间', null=True, blank=True)
    end_time = models.DateTimeField(verbose_name='结束时间', null=True, blank=True)
    
    def __str__(self):
        return f"#{self.id}.{self.name}"

class TodoRelationship(models.Model):
    from_Todo = models.ForeignKey(Todo, related_name='from_Todos', on_delete=models.CASCADE,verbose_name='源需求')
    to_Todo = models.ForeignKey(Todo, related_name='to_Todos', on_delete=models.CASCADE,verbose_name='衍生需求')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.from_Todo}->{self.to_Todo}"


class Note(models.Model):
    name = models.CharField(max_length=100, verbose_name='笔记名称')
    description = models.TextField(verbose_name='笔记',null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.name

