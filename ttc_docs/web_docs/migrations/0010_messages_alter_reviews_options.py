# Generated by Django 4.0 on 2022-01-01 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_docs', '0009_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth', models.CharField(max_length=50)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('message', models.TextField(max_length=500)),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
                'ordering': ('-date',),
            },
        ),
        migrations.AlterModelOptions(
            name='reviews',
            options={'ordering': ('-date',), 'verbose_name': 'Review', 'verbose_name_plural': 'Reviews'},
        ),
    ]
