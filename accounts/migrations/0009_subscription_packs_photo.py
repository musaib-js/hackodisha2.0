# Generated by Django 3.2.4 on 2022-06-10 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_subscription_packs'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription_packs',
            name='photo',
            field=models.ImageField(default='one.jpg', upload_to='media'),
        ),
    ]
