# Generated by Django 4.0.3 on 2022-04-01 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0004_delete_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
