# Generated by Django 2.2.24 on 2021-12-28 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0012_neighbourhood_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='neighbourhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='neighbour.NeighbourHood'),
        ),
    ]
