# Generated by Django 3.1.2 on 2020-11-29 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0014_auto_20201028_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]
