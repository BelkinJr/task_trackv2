# Generated by Django 3.0.4 on 2020-05-25 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
        ('invite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invite',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='invite', to='team.Team'),
        ),
    ]