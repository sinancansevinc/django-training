# Generated by Django 4.0.8 on 2023-01-10 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('sports', models.CharField(max_length=256)),
                ('estimated_price', models.DecimalField(decimal_places=2, default=50, max_digits=15)),
            ],
        ),
    ]
