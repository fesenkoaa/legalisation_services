# Generated by Django 4.0 on 2022-01-17 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_docs_ua', '0004_rename_advises_advisesua'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleua',
            name='advise',
            field=models.TextField(blank=True, max_length=9999, null=True, verbose_name='advise'),
        ),
    ]