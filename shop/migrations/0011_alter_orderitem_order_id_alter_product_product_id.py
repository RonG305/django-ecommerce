# Generated by Django 4.1.7 on 2023-04-23 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_product_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order_id',
            field=models.CharField(editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.BigAutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]