# Generated by Django 4.1.7 on 2023-03-17 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miss', '0002_candidate_age_alter_candidate_nom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_ref', models.CharField(default='', max_length=100)),
                ('ref_bsend', models.CharField(default='', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('statut', models.CharField(default='', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Souscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_ref', models.CharField(blank=True, max_length=140)),
                ('nbVote', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('nom', models.CharField(blank=True, max_length=140)),
                ('telephone', models.CharField(blank=True, max_length=140)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='miss.candidate')),
            ],
        ),
    ]