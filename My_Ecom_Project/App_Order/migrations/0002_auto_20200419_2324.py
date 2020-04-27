# Generated by Django 2.2.5 on 2020-04-19 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='update',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='orderitmes',
            new_name='orderitems',
        ),
        migrations.RemoveField(
            model_name='order',
            name='orderid',
        ),
        migrations.AddField(
            model_name='order',
            name='orderId',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
