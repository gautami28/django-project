# Generated by Django 3.2.2 on 2021-07-22 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20210722_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
