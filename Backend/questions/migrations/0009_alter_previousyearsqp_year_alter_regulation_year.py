# Generated by Django 4.1.1 on 2023-01-16 12:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_topic_active_topic_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='previousyearsqp',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1990), django.core.validators.MaxValueValidator(2023)]),
        ),
        migrations.AlterField(
            model_name='regulation',
            name='year',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(2010), django.core.validators.MaxValueValidator(2023)]),
        ),
    ]
