# Generated by Django 4.0.4 on 2022-06-01 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpost',
            name='content',
            field=models.TextField(max_length=500),
        ),
    ]
