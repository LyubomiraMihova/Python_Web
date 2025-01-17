# Generated by Django 4.2.4 on 2023-08-16 07:30

import django.core.validators
from django.db import migrations, models
import eventer_app.web.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)])),
                ('category', models.CharField(choices=[('SPORTS', 'Sports'), ('FESTIVALS', 'Festivals'), ('CONFERENCES', 'Conferences'), ('PERFORMING_ART', 'Performing Art'), ('CONCERTS', 'Concerts'), ('THEME_PARTY', 'Theme Party'), ('OTHER', 'Other')], max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateField(validators=[eventer_app.web.models.validate_date_not_in_past])),
                ('event_image', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, validators=[eventer_app.web.models.validate_name_only_letters])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(4)])),
                ('email', models.EmailField(max_length=45)),
                ('profile_picture', models.URLField(blank=True, null=True)),
                ('password', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(5), eventer_app.web.models.validate_password_at_least_one_digit])),
            ],
        ),
    ]
