from django.shortcuts import render
#from django.contrib.auth.models import Group#导入这2个表
#from django.contrib.auth.models import User
from rest_framework import viewsets#viewsets是定义视图的展示形式
from api.serializers import UserSerializer,GroupSerializer#导入这2个写了序列化的模块
# Create your views here.
from api.models import User,Group#导入我们创建的User,Group这些模块

class UserViewSet(viewsets.ModelViewSet):#创建一个方法继承viewsets
    """
           retrieve:
               Return a user instance.#返回一个用户实例。

           list:
               Return all users,odered by most recent joined.#返回所有用户，由最近加入的ORD。

           create:
               Create a new user.#创建新用户

           delete:
               Remove a existing user#删除用户

           partial_update:
               Update one or more fields on a existing user.#只更新一些字段。如更新邮箱哈，账号哈这些

           update:
               Update a user.#更新用户，全部更新


       """
    queryset=User.objects.all()#User.objects.all()就是查询User的表
    serializer_class=UserSerializer#这个是指向我们刚刚序列化User的类UserSerializer，serializer_class可以找到我们指向给那些字段
class GroupViewSet(viewsets.ModelViewSet):
    """
                retrieve:
                    Return a group instance.

                list:
                    Return all groups, ordered by most recently joined.

                create:
                    Create a new group.

                delete:
                    Remove an existing group.

                partial_update:
                    Update one or more fields on an existing group.

                update:
                    Update a group.
            """
    queryset=Group.objects.all()
    serializer_class=GroupSerializer