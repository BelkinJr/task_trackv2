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

from apps.base.constants import API_URL
from apps.user.views.user_create_view import UserView
from apps.user.views.user_login_view import UserLoginView
from apps.notes.views.note_create_view import NoteCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{API_URL}/users/', UserView.as_view(), name='users'),
    path(f'{API_URL}/login/', UserLoginView.as_view(), name='login'),
    path(f'{API_URL}/notes/', NoteCreateView.as_view(), name='note'),
]
