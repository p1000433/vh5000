# Generated by Django 2.1.7 on 2021-12-07 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bonus', '0005_winner_week'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='winner',
            options={'ordering': ['-week', '-prize_id']},
        ),
    ]
