# Generated by Django 4.1.7 on 2023-03-13 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_art_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='art',
            options={'ordering': ['-date']},
        ),
    ]
