# Generated by Django 5.0.1 on 2024-02-22 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_user_ise_active_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
