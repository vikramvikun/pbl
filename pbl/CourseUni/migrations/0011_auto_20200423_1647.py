# Generated by Django 3.0.5 on 2020-04-23 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CourseUni', '0010_auto_20200423_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='course_file',
            field=models.FileField(upload_to='pics'),
        ),
    ]
