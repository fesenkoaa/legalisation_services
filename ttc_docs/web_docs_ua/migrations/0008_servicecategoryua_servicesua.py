# Generated by Django 4.0 on 2022-01-31 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_docs_ua', '0007_articleua_advise'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCategoryUa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30, verbose_name='category')),
            ],
        ),
        migrations.CreateModel(
            name='ServicesUa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=50, verbose_name='service name')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='web_docs_ua.servicecategoryua', verbose_name='category')),
            ],
        ),
    ]
