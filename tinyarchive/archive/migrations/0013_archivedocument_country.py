# Generated by Django 4.0.5 on 2022-07-31 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0012_archivedocument_size_archivedocument_usage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivedocument',
            name='country',
            field=models.CharField(blank='True', max_length=50),
        ),
    ]
