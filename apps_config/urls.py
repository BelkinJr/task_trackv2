"""task_track_v2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from apps.user.views.user_create_view import UserCreateView
from apps.user.views.user_list_view import UserListView
from apps.user.views.user_login_view import UserLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', UserCreateView.as_view()),
    path('userlist/', UserListView.as_view()),
    path('login/', UserLoginView.as_view()),
]
