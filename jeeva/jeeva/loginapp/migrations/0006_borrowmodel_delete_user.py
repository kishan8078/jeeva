# Generated by Django 4.2.4 on 2023-12-22 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0005_alter_user_user_email_alter_user_user_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('adhaar_number', models.IntegerField()),
                ('category', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
