# Generated by Django 4.2.16 on 2024-11-16 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['id'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]
