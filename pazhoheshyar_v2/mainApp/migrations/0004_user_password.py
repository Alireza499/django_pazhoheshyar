# Generated by Django 4.1.5 on 2023-01-23 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_thesis_pdf_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=0, max_length=16),
            preserve_default=False,
        ),
    ]
