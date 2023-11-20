# Generated by Django 4.2.5 on 2023-11-20 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tailer', '0011_customer_pant_length_customer_pant_width'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='cloth_color',
            field=models.CharField(blank=True, choices=[('red', 'Red'), ('green', 'Green'), ('blue', 'Blue'), ('yellow', 'Yellow'), ('magenta', 'Magenta'), ('cyan', 'Cyan'), ('orange', 'Orange'), ('purple', 'Purple'), ('darkgreen', 'Dark Green'), ('navy', 'Navy'), ('pink', 'Pink'), ('saddlebrown', 'Saddle Brown'), ('brown', 'Brown'), ('gray', 'Gray'), ('black', 'Black')], max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='cloth_price',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
