# Generated by Django 3.2.9 on 2022-10-23 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_answer_responses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='choices',
            field=models.ManyToManyField(blank=True, related_name='choices', to='survey.Choices'),
        ),
    ]
