# Generated by Django 3.2.9 on 2021-12-03 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniapp', '0005_auto_20211203_2338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='product',
            new_name='products',
        ),
    ]
