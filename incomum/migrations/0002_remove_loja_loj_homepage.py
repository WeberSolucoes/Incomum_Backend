# Generated by Django 5.0.7 on 2024-07-26 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incomum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loja',
            name='loj_homepage',
        ),
    ]
