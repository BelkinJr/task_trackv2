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
from apps.user.views.user_view import UserView
from apps.user.views.user_login_view import UserLoginView
from apps.notes.views.note_view import NoteView
from apps.team.views.team_view import TeamView
from apps.invite.views.invite_view import InviteView
from apps.user.views.get_user_by_username_view import GetUserByUsernameView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{API_URL}/users/', UserView.as_view(), name='users'),
    path(f'{API_URL}/login/', UserLoginView.as_view(), name='login'),
    path(f'{API_URL}/notes/', NoteView.as_view(), name='note'),
    path(f'{API_URL}/teams/<uuid:team_id>/generate_invite/', InviteView.as_view(), name='generate_invite'),
    path(f'{API_URL}/teams/', TeamView.as_view(), name='team'),
    # path(f'{API_URL}/invites/', InviteView.as_view(), name='invite'),
]


