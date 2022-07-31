from django.db import models

from django.contrib.auth.models import User


class Training(models.Model):

    class TrainingStatusChoice(models.TextChoices):
        PLANNED = 'P', 'Запланирована'
        COMPLETED = 'C', 'Завершена'
        SKIPPED = 'S', 'Пропущена'

    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        related_name='trainings',
        on_delete=models.CASCADE,
    )
    date = models.DateField(
        verbose_name='Дата тренировки',
    )
    sets = models.ManyToManyField(
        'ExerciseSet',
        verbose_name='Подходы',
    )
    comment = models.TextField(
        verbose_name='Комментарии к тренировке',
        null=True,
        blank=True,
    )
    # TODO:
    #  Возможно добавить комментарии до и после тренировки?
    status = models.CharField(
        max_length=1,
        choices=TrainingStatusChoice.choices,
        default=TrainingStatusChoice.PLANNED,
        verbose_name='Статус тренировки',
    )

    class Meta:
        unique_together = (('user', 'date'),)
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'
        ordering = ['-date']

    def __str__(self):
        return f'Тренировка пользователя {self.user.username} от {self.date}'
