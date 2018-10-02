#from django.contrib.auth.models import Group#导入User，Group这2个表
#from django.contrib.auth.models import User
from rest_framework import serializers#导入serializers这个模块，serializers这个模块可以把表格序列化
from api.models import User,Group#导入我们创建的User,Group这些模块

class UserSerializer(serializers.HyperlinkedModelSerializer):#定义一个类，这个类继承了serializers调用HyperlinkedModelSerializer
    class Meta:
        #再定义一个原类
        model=User
        #然后model指向User
        fields=("url","username","email","id")#然后定义User这个表的一些字段，url，email等这些
class GroupSerializer(serializers.HyperlinkedModelSerializer):#定义Group的序列
    class Meta:
        model=Group
        fields=("url","name","id")#定义url，name字段
#这个是数据库的初始化操作