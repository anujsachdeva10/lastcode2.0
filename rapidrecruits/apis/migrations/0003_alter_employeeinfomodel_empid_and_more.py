# Generated by Django 4.1 on 2022-08-18 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_employeeinfomodel_department_employeeinfomodel_empid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeinfomodel',
            name='empid',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='employeeinfomodel',
            unique_together={('college', 'empid')},
        ),
    ]