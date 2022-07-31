from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    """Класс упражнения для справочника упражнений"""

    title = models.CharField(
        max_length=128,
        verbose_name='Название',
        unique=True,
    )
    technic = models.TextField(
        verbose_name='Техника выполнения',
    )
    # TODO:
    #  muscle_groups - manytomany со ссылкой на спрвочник мышц
    #  extra_muscle_groups - аналогично
    #  equipment - (many_to_many or foreign)? со ссылкой на справочник оборудования
    #  стоит ли добавлять базовое/изолирующее, силовое/растяжка/кардио?
    created_by = models.ForeignKey(
        User,
        related_name='exercises',
        verbose_name='Автор',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    created_on = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'
        ordering = ['-created_on']

    def __str__(self):
        return f'Упражнение "{self.title}"'
