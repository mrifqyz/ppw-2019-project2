# Generated by Django 2.2.6 on 2019-12-08 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danusan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='danusan',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]
