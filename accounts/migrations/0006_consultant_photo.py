# Generated by Django 3.2.4 on 2022-04-28 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20220427_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultant',
            name='photo',
            field=models.ImageField(default='one.jpg', upload_to='media'),
        ),
    ]
