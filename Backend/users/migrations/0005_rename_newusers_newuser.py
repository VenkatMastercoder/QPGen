# Generated by Django 4.1.1 on 2023-02-19 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_newusers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewUsers',
            new_name='NewUser',
        ),
    ]
