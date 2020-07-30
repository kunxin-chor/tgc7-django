# Generated by Django 2.2.14 on 2020-07-27 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_book_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cost',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
