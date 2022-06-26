# Generated by Django 3.2.6 on 2021-08-18 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_name', models.CharField(max_length=200)),
                ('candidate_party', models.CharField(max_length=20)),
                ('candidate_email', models.EmailField(max_length=200)),
                ('candidate_spent_daily', models.FloatField()),
                ('candidate_spent_monthly', models.FloatField()),
                ('candidate_spent_total', models.FloatField()),
            ],
        ),
    ]
