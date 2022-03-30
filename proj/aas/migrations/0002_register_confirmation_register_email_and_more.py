# Generated by Django 4.0.3 on 2022-03-30 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='confirmation',
            field=models.CharField(default=3, max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='email',
            field=models.EmailField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='register',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]