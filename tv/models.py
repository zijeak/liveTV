from django.db import models

# Create your models here.
class channel(models.Model):
    name = models.CharField(max_length=200,verbose_name='频道名称',null=False)
    address = models.CharField(max_length=1000,verbose_name='频道串流',null=False)

    category = models.ForeignKey('Category')


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='分类名称', null=False)

    def __str__(self):
        return self.name


class Notice(models.Model):
    title = models.CharField(max_length=200, verbose_name='通知标题', null=False)
    content = models.CharField(max_length=200,verbose_name='通知内容',null = True)

    def __str__(self):
        return self.title;
