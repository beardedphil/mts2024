# Generated by Django 3.1.4 on 2024-01-22 14:39

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=25)),
                ('article_link', models.URLField(unique=True)),
                ('image_link', models.URLField()),
                ('pub_date', models.DateField()),
                ('keywords', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, size=None)),
            ],
        ),
    ]
