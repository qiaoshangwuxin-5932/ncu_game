"""NcuGamer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from Gamer import views
from django.views.decorators.csrf import csrf_exempt
from Gamer.userAndQuestion import user,pushScore

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'user/',csrf_exempt(user.Username.as_view()),name='用户视图'),
    path('score/',pushScore.pushScore,name='提交分数'),
    path('choise/',views.Choise,name='返回题目'),
    path('image/',views.ReturnImage,name='等级图片'),
    path('nine/',views.nine,name='九宫格')
]



