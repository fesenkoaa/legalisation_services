# Generated by Django 4.0 on 2022-01-13 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_docs', '0022_contact_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='last_name',
        ),
    ]