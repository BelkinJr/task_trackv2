from django.db import models
from django.db.models import QuerySet
from apps.base.models.base import BaseModel
from apps.team.models.user_team import UserTeam
from apps.user.models.user import User


class Team(BaseModel):

    team_name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='teams', through=UserTeam)
    creator_id = models.UUIDField()

    class Meta:
        db_table = 'team'
        verbose_name = "team"

    def add_user(self, user: User) -> None:
        assert isinstance(user, User), f"{user} is given"
        if not self.users.filter(id=user.id):
            UserTeam.objects.create(team_id=self.id, user_id=user.id)

    def add_users(self, users_qs: QuerySet) -> None:
        assert isinstance(users_qs.first(), User), f"{users_qs.first()} is given"
        if users_qs.exists():
            not_added_users_id_qs = users_qs.exclude(id__in=self.users.values_list("id", flat=True)).values("id")
            UserTeam.objects.bulk_create([UserTeam(user_id=user_id["id"], team_id=self.id) for user_id in list(not_added_users_id_qs)])

    def remove_user(self, user: User) -> None:
        assert isinstance(user, User), f"{user} is given"
        if self.users.filter(id=user.id):
            user.user_teams.get(team_id=self.id).delete()
