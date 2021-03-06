# Generated by Django 3.1.2 on 2020-10-07 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=200)),
                ('original_price', models.IntegerField()),
                ('sale_price', models.IntegerField()),
                ('slug', models.SlugField()),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
