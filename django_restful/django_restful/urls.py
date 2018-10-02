"""django_restful URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path#导入path做路径配置
from django.conf.urls import include#导入include进行添加路径
from rest_framework import routers#导入routers做路由的配置
from api import views#导入视图
from rest_framework.schemas import get_schema_view#导入辅助函数
from rest_framework_swagger.renderers import SwaggerUIRenderer,OpenAPIRenderer

schema_view=get_schema_view(title='刘学良用户增删改查的接口API文档',renderer_classes=[OpenAPIRenderer,SwaggerUIRenderer])#定义api文档名称和导入SwaggerUIRenderer,OpenAPIRenderer

router=routers.DefaultRouter()#生成一个路由对象
router.register(r'Users',views.UserViewSet)#然后使用register进行配置我们的视图，r'urls'当我们输入urls就会指向views.UserViewSet视图
router.register(r'Groups',views.GroupViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),#path是添加路径。''空路径。是在http://127.0.0.1:8000/后面添加router.urls，router.urls就是router这个调用urls，urls就是我们上面添加的urls，groups这2个视图
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),#这里是在http://127.0.0.1:8000/api-auth/添加'rest_framework.urls路径
    path('docs/',schema_view,name='docs')#然后配置路径
]

