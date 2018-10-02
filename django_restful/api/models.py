from django.db import models

# Create your models here.
class User(models.Model):#定义User这个类，然后继承models这个模块并且调用model
    username=models.CharField(max_length=100)#定义名称这个字段类型为字符串并且100字段
    email=models.CharField(max_length=100)#CharField字符类型
    #groups=models.CharField(max_length=100)
    #id=models.IntegerField(max_length=100)#IntegerField是integer类型，

    def __str__(self):#__str__方法是美化字段
        return self.username

class Group(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name