from django.db import models

from exercises.models import Exercise


class ExerciseSet(models.Model):

    exercise = models.ForeignKey(
        Exercise,
        verbose_name='Упражнение',
        related_name='sets',
        on_delete=models.CASCADE,
    )
    reps_plan = models.PositiveSmallIntegerField(
        verbose_name='Запланированное количество повторений',
        null=True,
        blank=True,
    )
    reps_fact = models.PositiveSmallIntegerField(
        verbose_name='Фактическое количество повторений',
        null=True,
        blank=True,
    )
    weight_plan = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        verbose_name='Запланированный вес',
        null=True,
        blank=True,
    )
    weight_fact = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        verbose_name='Фактический вес',
        null=True,
        blank=True,
    )
    is_done = models.BooleanField(
        verbose_name='Выполнено',
        default=False,
    )

    class Meta:
        verbose_name = 'Подход'
        verbose_name_plural = 'Подходы'

    def __str__(self):
        return f'Подход упражнения {self.exercise.title}'
