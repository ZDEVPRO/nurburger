# Generated by Django 4.1.6 on 2023-07-18 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_category_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Kategoriyalar', 'verbose_name_plural': 'Kategoriyalar'},
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]