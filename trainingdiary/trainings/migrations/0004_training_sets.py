# Generated by Django 4.0.6 on 2022-07-31 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0003_alter_training_unique_together_exerciseset'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='sets',
            field=models.ManyToManyField(to='trainings.exerciseset', verbose_name='Подходы'),
        ),
    ]
