# Generated by Django 3.0.5 on 2020-04-23 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CourseUni', '0016_auto_20200423_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='course_file',
            field=models.FileField(upload_to=''),
        ),
    ]