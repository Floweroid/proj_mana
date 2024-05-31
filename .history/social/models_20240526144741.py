from django.db import models

class Person(models.Model):
    lName = models.CharField(max_length=100, verbose_name='姓氏')
    mid = models.CharField(max_length=100, verbose_name='中间名', null=True, blank=True)
    fName = models.CharField(max_length=100, verbose_name='名字')
    hometown = models.CharField(max_length=100, verbose_name='家乡', null=True, blank=True)
    description = models.TextField(verbose_name='描述', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return f"{self.fName} {self.lName}"

class SocialRelationship(models.Model):
    from_person = models.ForeignKey(Person, related_name='from_relationships', on_delete=models.CASCADE, verbose_name='从')
    to_person = models.ForeignKey(Person, related_name='to_relationships', on_delete=models.CASCADE, verbose_name='到')
    relation = models.CharField(max_length=100, verbose_name='关系类型')

    def __str__(self):
        return f"{self.from_person} -> {self.to_person}: {self.relation}"
