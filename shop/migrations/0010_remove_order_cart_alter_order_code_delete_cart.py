# Generated by Django 4.2.4 on 2023-09-18 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_remove_sellproduct_product_cart_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='a6026c39dfd0', max_length=25),
        ),
        migrations.DeleteModel(
            name='cart',
        ),
    ]
