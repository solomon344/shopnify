# Generated by Django 4.2.4 on 2023-09-18 00:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0007_alter_order_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='by',
        ),
        migrations.AddField(
            model_name='order',
            name='by',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='dbf231e22236', max_length=25),
        ),
    ]