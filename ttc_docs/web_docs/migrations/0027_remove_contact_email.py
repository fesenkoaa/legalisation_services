# Generated by Django 4.0 on 2022-01-17 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_docs', '0026_advises'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
    ]