# Generated by Django 4.1.7 on 2023-03-18 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miss', '0008_remove_souscription_candidat'),
    ]

    operations = [
        migrations.AddField(
            model_name='souscription',
            name='candidat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='miss.candidat'),
        ),
    ]
