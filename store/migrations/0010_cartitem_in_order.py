# Generated by Django 3.1.1 on 2020-09-03 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20200903_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='in_order',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
