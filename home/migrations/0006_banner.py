# Generated by Django 4.1.6 on 2023-07-18 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=600)),
                ('title', models.CharField(max_length=600)),
                ('price', models.CharField(max_length=600)),
                ('image', models.ImageField(upload_to='images/')),
                ('button_title', models.CharField(max_length=600)),
                ('button_link', models.CharField(max_length=2000)),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banner',
            },
        ),
    ]
