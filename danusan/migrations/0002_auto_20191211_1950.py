# Generated by Django 2.2.6 on 2019-12-11 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('danusan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='danusan',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='danusan',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]
