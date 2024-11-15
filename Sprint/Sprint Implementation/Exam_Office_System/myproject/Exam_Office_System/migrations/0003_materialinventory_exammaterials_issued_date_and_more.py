# Generated by Django 5.1.1 on 2024-11-08 21:22

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exam_Office_System', '0002_alter_student_expelled_alter_student_hall_clearance_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_type', models.CharField(choices=[('AnswerScripts', 'Answer Scripts'), ('LooseSheets', 'Extra Loose Sheets')], max_length=50, unique=True)),
                ('stock_quantity', models.IntegerField()),
                ('threshold_quantity', models.IntegerField(default=200)),
            ],
        ),
        migrations.AddField(
            model_name='exammaterials',
            name='issued_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exammaterials',
            name='last_updated',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='exammaterials',
            name='material_type',
            field=models.CharField(choices=[('AnswerScripts', 'Answer Scripts'), ('LooseSheets', 'Extra Loose Sheets')], max_length=50),
        ),
        migrations.CreateModel(
            name='MaterialDistributionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_type', models.CharField(choices=[('AnswerScripts', 'Answer Scripts'), ('LooseSheets', 'Extra Loose Sheets')], max_length=50)),
                ('quantity_issued', models.IntegerField()),
                ('distribution_date', models.DateField(default=datetime.date.today)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='distribution_logs', to='Exam_Office_System.exam')),
            ],
        ),
    ]