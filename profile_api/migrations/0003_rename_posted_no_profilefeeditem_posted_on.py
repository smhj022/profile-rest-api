# Generated by Django 3.2.5 on 2021-07-31 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_api', '0002_profilefeeditem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilefeeditem',
            old_name='posted_no',
            new_name='posted_on',
        ),
    ]