# Generated by Django 4.0 on 2022-01-31 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_docs', '0031_alter_contact_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='title')),
                ('images', models.ImageField(upload_to='', verbose_name='image')),
            ],
        ),
    ]
