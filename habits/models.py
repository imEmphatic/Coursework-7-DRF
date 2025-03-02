from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    """Модель привычки, содержащая информацию о её названии, месте, времени, действии и других параметрах"""

    FREQUENCY_UNITS = [
        ("minutes", "минуты"),
        ("hours", "часы"),
        ("days", "дни"),
    ]

    name = models.CharField(
        max_length=100, verbose_name="Название привычки", **NULLABLE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Cоздатель привычки",
        **NULLABLE,
    )
    place = models.CharField(max_length=75, verbose_name="Место привычки")
    time = models.TimeField(verbose_name="Время дня привычки")
    action = models.CharField(max_length=75, verbose_name="Действие привычки")
    is_nice_habit = models.BooleanField(verbose_name="Признак приятной привычки")
    related_habit = models.ForeignKey(
        "self", on_delete=models.SET_NULL, **NULLABLE, verbose_name="Связанная привычка"
    )
    frequency_number = models.PositiveIntegerField(verbose_name="Количество раз")
    frequency_unit = models.CharField(
        max_length=10,
        choices=FREQUENCY_UNITS,
        default="days",
        verbose_name="Единицы измерения",
    )
    reward = models.CharField(max_length=200, verbose_name="Вознаграждение", **NULLABLE)
    duration = models.DurationField(verbose_name="Длительность действия")
    is_public = models.BooleanField(default=True, verbose_name="Публичная")

    def __str__(self):
        """Возвращает строковое представление привычки (её название)"""
        return self.name

    class Meta:
        """Метаданные модели Habit"""

        verbose_name = "привычка"
        verbose_name_plural = "привычки"
