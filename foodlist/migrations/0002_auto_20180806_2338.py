# Generated by Django 2.0.7 on 2018-08-06 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='food',
            name='item_name',
            field=models.CharField(max_length=200),
        ),
    ]