# Generated by Django 4.1.5 on 2023-01-24 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_rename_type_user_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='thesis',
            name='davar1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='davar1', to='mainApp.user'),
        ),
        migrations.AddField(
            model_name='thesis',
            name='davar2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='davar2', to='mainApp.user'),
        ),
        migrations.AddField(
            model_name='thesis',
            name='davar3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='davar3', to='mainApp.user'),
        ),
        migrations.AddField(
            model_name='thesis',
            name='davar4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='davar4', to='mainApp.user'),
        ),
    ]