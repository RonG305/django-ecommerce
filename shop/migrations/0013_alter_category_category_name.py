# Generated by Django 4.1.7 on 2023-04-24 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_alter_category_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(choices=[('Computing', 'computing'), ('Electronics', 'electronics'), ('Sporting', 'sporting'), ('Fashion', 'fashion'), ('Automobile', 'automobile'), ('Toys & Games', 'toys & games'), ('Phones&Tablets', 'phones&tablets'), ('Musical', 'Musical')], max_length=255),
        ),
    ]
