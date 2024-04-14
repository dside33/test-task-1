# Generated by Django 3.2.16 on 2024-04-12 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_test_iscorrect'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_name', models.CharField(max_length=100)),
                ('test', models.ManyToManyField(to='tests.Test')),
            ],
        ),
    ]