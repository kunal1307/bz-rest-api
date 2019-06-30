# Generated by Django 2.2.2 on 2019-06-30 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(default='Active', max_length=10)),
                ('created', models.DateTimeField()),
                ('last_modified_date', models.DateTimeField(blank=True, null=True)),
                ('agency', models.CharField(blank=True, max_length=100, null=True)),
                ('logo_url', models.CharField(blank=True, max_length=1024, null=True)),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
            ],
        ),
    ]