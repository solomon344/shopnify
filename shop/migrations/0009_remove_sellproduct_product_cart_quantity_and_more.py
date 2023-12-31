# Generated by Django 4.2.4 on 2023-09-18 01:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0008_remove_cart_by_order_by_alter_order_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellproduct',
            name='product',
        ),
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(to='shop.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='e00a7878b22b', max_length=25),
        ),
        migrations.DeleteModel(
            name='Orderhistory',
        ),
        migrations.DeleteModel(
            name='sellProduct',
        ),
    ]
