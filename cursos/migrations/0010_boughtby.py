# Generated by Django 4.0.4 on 2022-06-27 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cursos', '0009_remove_course_presentationvideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoughtBy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bought_by', to='cursos.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bought_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]