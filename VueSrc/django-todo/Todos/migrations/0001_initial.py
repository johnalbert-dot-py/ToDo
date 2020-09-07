# Generated by Django 3.1 on 2020-09-07 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
            ],
        ),
    ]