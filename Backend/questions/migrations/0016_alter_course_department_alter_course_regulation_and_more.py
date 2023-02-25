# Generated by Django 4.1.1 on 2023-02-22 14:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0015_question_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='courses', to='questions.department'),
        ),
        migrations.AlterField(
            model_name='course',
            name='regulation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='courses', to='questions.regulation'),
        ),
        migrations.AlterField(
            model_name='department',
            name='degree',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='departments', to='questions.degree'),
        ),
        migrations.AlterField(
            model_name='department',
            name='hod',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='departments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='department',
            name='programme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='departments', to='questions.programme'),
        ),
        migrations.AlterField(
            model_name='facultieshandling',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='faculties', to='questions.course'),
        ),
        migrations.AlterField(
            model_name='facultieshandling',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='faculties', to='questions.subject'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='outcome_btl',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lessons', to='questions.bloomstaxonomylevel'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lessons', to='questions.subject'),
        ),
        migrations.AlterField(
            model_name='question',
            name='btl',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='questions', to='questions.bloomstaxonomylevel'),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='questions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='questions', to='questions.lesson'),
        ),
        migrations.AlterField(
            model_name='question',
            name='mark',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='questions', to='questions.markrange'),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='syllabuses', to='questions.course'),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='syllabuses', to='questions.lesson'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='topics', to='questions.lesson'),
        ),
    ]
