# Generated by Django 2.2.7 on 2019-12-12 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bantuan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pertanyaan', models.CharField(max_length=100)),
                ('jawaban', models.TextField(blank=True)),
                ('nama', models.CharField(max_length=50)),
                ('waktu', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
