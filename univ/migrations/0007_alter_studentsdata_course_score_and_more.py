# Generated by Django 5.1.1 on 2024-09-28 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('univ', '0006_alter_studentsdata_course_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsdata',
            name='course_score',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentsdata',
            name='score10',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='studentsdata',
            name='score12',
            field=models.FloatField(default=0.0),
        ),
    ]
