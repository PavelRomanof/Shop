# Generated by Django 3.2.9 on 2021-12-03 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniapp', '0004_somemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='for_anonymous_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='in_order',
            field=models.BooleanField(default=False),
        ),
    ]
