# Generated by Django 3.0.4 on 2020-06-19 22:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20200525_2002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('invite', '0004_auto_20200601_1038'),
    ]

    operations = [
        migrations.CreateModel(
            name='InviteUserToTeam',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('ACC', 'accepted'), ('DEC', 'declined'), ('PEN', 'pending')], default='PEN', max_length=31)),
                ('token', models.CharField(max_length=255, null=True)),
                ('token_date_accepted', models.DateTimeField(null=True)),
                ('token_date_expired', models.DateTimeField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='invites', to='team.Team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='invites', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'invite',
                'db_table': 'invite',
            },
        ),
        migrations.DeleteModel(
            name='Invite',
        ),
    ]
