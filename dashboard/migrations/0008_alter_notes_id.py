# Generated by Django 3.2.2 on 2021-07-22 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_alter_notes_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='id',
            field=models.DateTimeField(primary_key=True, serialize=False),
        ),
    ]
