# Generated by Django 4.1.5 on 2023-01-24 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_thesis_davar1_thesis_davar2_thesis_davar3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thesis',
            name='davar3',
        ),
        migrations.RemoveField(
            model_name='thesis',
            name='davar4',
        ),
        migrations.AddField(
            model_name='thesis',
            name='proposal_davar1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proposal_davar1', to='mainApp.user'),
        ),
        migrations.AddField(
            model_name='thesis',
            name='proposal_davar2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proposal_davar2', to='mainApp.user'),
        ),
        migrations.AddField(
            model_name='thesis',
            name='proposal_davar3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proposal_davar3', to='mainApp.user'),
        ),
        migrations.AddField(
            model_name='thesis',
            name='proposal_davar4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proposal_davar4', to='mainApp.user'),
        ),
    ]
