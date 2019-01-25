# Generated by Django 2.0 on 2018-12-31 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicineallot',
            name='actual_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='medicineallot',
            name='actual_qty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='medicineallot',
            name='alloted_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='medicineallot',
            name='alloted_qty',
            field=models.IntegerField(default=0),
        ),
    ]
