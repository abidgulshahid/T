# Generated by Django 4.2.5 on 2023-10-22 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tailer', '0009_rename_tailor_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='payment',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='recieved',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=255, null=True),
        ),
    ]
