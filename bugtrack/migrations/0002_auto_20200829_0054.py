# Generated by Django 3.1 on 2020-08-29 00:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bugtrack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='assigned_to',
            field=models.ForeignKey(blank='True', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ticket',
            name='completed_by',
            field=models.ForeignKey(blank='True', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='completed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ticket',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
