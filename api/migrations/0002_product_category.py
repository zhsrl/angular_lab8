# Generated by Django 4.0.3 on 2022-04-13 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('PHONES', 'phones'), ('LAPTOPS', 'laptops'), ('TV', 'tv'), ('PC', 'pc')], default='PHONES', max_length=9),
        ),
    ]