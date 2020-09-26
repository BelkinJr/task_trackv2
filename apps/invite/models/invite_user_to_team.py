from django.db import models
from apps.user.models import User
from apps.team.models import Team
from apps.base.models.base import BaseModel


class InviteUserToTeam(BaseModel):
    INVITE_STATUS_ACCEPTED = 'ACC'
    INVITE_STATUS_DECLINED = 'DEC'
    INVITE_STATUS_PENDING = 'PEN'

    user = models.ForeignKey(User, related_name='invites', on_delete=models.DO_NOTHING)
    team = models.ForeignKey(Team, related_name='invites', on_delete=models.DO_NOTHING)
    status = models.CharField(choices=(
        (INVITE_STATUS_ACCEPTED, 'accepted'),
        (INVITE_STATUS_DECLINED, 'declined'),
        (INVITE_STATUS_PENDING, 'pending'),
    ), default=INVITE_STATUS_PENDING, max_length=31)
    token = models.CharField(max_length=255, null=True)
    token_date_accepted = models.DateTimeField(null=True)
    token_date_expired = models.DateTimeField()

    class Meta:
        db_table = 'invite'
        verbose_name = 'invite'
