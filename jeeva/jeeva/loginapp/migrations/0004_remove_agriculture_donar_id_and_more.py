# Generated by Django 4.2.4 on 2023-12-21 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0003_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agriculture',
            name='donar_id',
        ),
        migrations.RemoveField(
            model_name='education',
            name='donar_id',
        ),
        migrations.RemoveField(
            model_name='foodandhealth',
            name='donar_id',
        ),
        migrations.RemoveField(
            model_name='smallenterprise',
            name='donar_id',
        ),
        migrations.RemoveField(
            model_name='vehicles',
            name='donar_id',
        ),
        migrations.AddField(
            model_name='user',
            name='user_phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_password',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='donar',
        ),
    ]
