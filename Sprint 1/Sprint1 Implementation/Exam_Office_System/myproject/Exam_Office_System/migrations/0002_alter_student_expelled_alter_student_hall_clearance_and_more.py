# Generated by Django 5.0.6 on 2024-10-31 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exam_Office_System', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='expelled',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='hall_clearance',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='library_clearance',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
