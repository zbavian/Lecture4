# Generated by Django 5.0.6 on 2024-06-13 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='first',
            field=models.CharField(max_length=64),
        ),
    ]
