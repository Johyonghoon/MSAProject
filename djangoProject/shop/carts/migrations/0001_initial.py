# Generated by Django 4.1.3 on 2022-11-30 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=120, unique=True)),
                ('nickname', models.CharField(max_length=20, unique=True)),
                ('passwd', models.CharField(max_length=255)),
                ('point', models.IntegerField()),
            ],
            options={
                'db_table': 'shop_carts',
            },
        ),
    ]
