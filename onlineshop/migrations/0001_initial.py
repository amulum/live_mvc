# Generated by Django 3.0 on 2019-12-12 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_path', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DescribeProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descipt', models.TextField(verbose_name=2000)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineshop.Product')),
            ],
        ),
    ]
