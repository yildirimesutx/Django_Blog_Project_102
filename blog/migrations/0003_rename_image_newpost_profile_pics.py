# Generated by Django 4.0.4 on 2022-06-02 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_newpost_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newpost',
            old_name='image',
            new_name='profile_pics',
        ),
    ]
