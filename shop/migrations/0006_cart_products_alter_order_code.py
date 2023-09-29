# Generated by Django 4.2.4 on 2023-09-17 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_remove_cart_products_alter_order_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(to='shop.sellproduct'),
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='23be6467e5dc', max_length=25),
        ),
    ]
