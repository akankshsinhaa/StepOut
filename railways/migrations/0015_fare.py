# Generated by Django 4.0.8 on 2022-11-04 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('railways', '0014_trains_type_distance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('base_fare', models.IntegerField()),
                ('sl_km', models.IntegerField()),
                ('ac_km', models.IntegerField()),
            ],
        ),
    ]