# Generated by Django 5.0.6 on 2024-06-28 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
