from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Todo(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    STATUS_CHOICES = (
        ('常态化', 'Normal'),
        ('已取消', 'Cancelled'),
        ('已完成', 'Completed'),
        ('进行中', 'In Progress'),
        ('未开始', 'Not Started'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name='Status', default='未开始')
    description = models.TextField(verbose_name='Description', null=True, blank=True)
    priority = models.IntegerField(verbose_name='Priority', default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created Time')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated Time')
    # parents = models.ManyToManyField('self', through='TodoRelationship', symmetrical=False, verbose_name='Parent Requirements')

    start_time = models.DateTimeField(verbose_name='Start Time', null=True, blank=True)
    end_time = models.DateTimeField(verbose_name='End Time', null=True, blank=True)
    
    def __str__(self):
        return f"#{self.id}.{self.name}"

class TodoRelationship(models.Model):
    from_Todo = models.ForeignKey(Todo, related_name='from_Todos', on_delete=models.CASCADE, verbose_name='Belong to')
    to_Todo = models.ForeignKey(Todo, related_name='to_Todos', on_delete=models.CASCADE, verbose_name='Derived')
    from_status = models.CharField(max_length=10, choices=Todo.STATUS_CHOICES, verbose_name='From Status', default='未开始')
    to_status = models.CharField(max_length=10, choices=Todo.STATUS_CHOICES, verbose_name='To Status', default='未开始')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.from_Todo}->{self.to_Todo}"

# class Note(models.Model):
#     name = models.CharField(max_length=100, verbose_name='笔记名称')
#     description = models.TextField(verbose_name='笔记',null=True)
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

#     def __str__(self):
#         return self.name
    

    
class Person(models.Model):
    lName = models.CharField(max_length=100, verbose_name='Last Name')
    mid = models.CharField(max_length=100, verbose_name='Middle Name', null=True, blank=True)
    fName = models.CharField(max_length=100, verbose_name='First Name')
    hometown = models.CharField(max_length=100, verbose_name='Hometown', null=True, blank=True)
    description = models.TextField(verbose_name='Description', null=True, blank=True)
    birthdate = models.DateField(verbose_name='Birthdate', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

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

class TodoPersonRelation(models.Model):
    person = models.ForeignKey('person', on_delete=models.CASCADE, verbose_name='Person')
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, verbose_name='Todo')
    
    def __str__(self):
        return f"Todo: {self.todo_id}, Person: {self.person}"



# Receiver
@receiver(post_save, sender=Todo)
def update_relationship_status(sender, instance, **kwargs):
    TodoRelationship.objects.filter(from_Todo=instance).update(from_status=instance.status)
    TodoRelationship.objects.filter(to_Todo=instance).update(to_status=instance.status)
    
    