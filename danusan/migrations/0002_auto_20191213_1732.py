# Generated by Django 2.2.6 on 2019-12-13 10:32

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('danusan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nama', models.CharField(max_length=300)),
                ('Review', models.CharField(max_length=30000)),
                ('Time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='danusan',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='nama'),
        ),
        migrations.CreateModel(
            name='DanusanDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=30000)),
                ('price', models.PositiveIntegerField()),
                ('gambar', models.CharField(max_length=30000)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='nama')),
                ('detail', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='danusan.Danusan')),
            ],
            options={
                'ordering': ['nama'],
            },
        ),
    ]
