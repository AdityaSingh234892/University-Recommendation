# Generated by Django 5.1.1 on 2024-09-28 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('univ', '0007_alter_studentsdata_course_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsdata',
            name='course_score',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
