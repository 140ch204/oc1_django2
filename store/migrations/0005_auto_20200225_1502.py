# Generated by Django 3.0.3 on 2020-02-25 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='album',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='store.Album'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='contact',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='store.Contact'),
            preserve_default=False,
        ),
    ]
