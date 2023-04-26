# Generated by Django 4.1.7 on 2023-04-17 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_product_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='active',
        ),
        migrations.RemoveField(
            model_name='category',
            name='category_description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category'),
        ),
    ]