# Generated by Django 2.0.7 on 2018-08-08 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodlist', '0004_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='sub_cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='foodlist.Subcategory'),
        ),
    ]