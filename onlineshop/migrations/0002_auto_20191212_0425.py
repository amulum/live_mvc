# Generated by Django 3.0 on 2019-12-12 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='describeproduct',
            name='descipt',
            field=models.TextField(max_length=2000),
        ),
    ]
