# Generated by Django 2.0.7 on 2018-08-08 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodlist', '0005_food_sub_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='sub_cat',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='foodlist.Subcategory'),
            preserve_default=False,
        ),
    ]