# Generated by Django 4.1.1 on 2023-02-08 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_alter_question_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quesions', to='questions.lesson'),
        ),
    ]
