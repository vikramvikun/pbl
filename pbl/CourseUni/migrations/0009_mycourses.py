# Generated by Django 3.0.5 on 2020-04-21 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CourseUni', '0008_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='mycourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mycourse', models.CharField(max_length=200)),
            ],
        ),
    ]
