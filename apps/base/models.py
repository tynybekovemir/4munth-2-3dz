from django.db import models

# Create your models here.
class Settings(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name="Логотип"
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = "Заголовок сайта"
    )
    description = models.TextField(
        verbose_name="Описание",
    )
    image = models.ImageField(
        upload_to='slide/',
        verbose_name="слайд"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Основные настройки сайта"
        verbose_name_plural = "Основные настройки сайта"


class About(models.Model):
    image = models.ImageField(
        upload_to='about/',
        verbose_name="Фото О нас"
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = "Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание",
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

class Course(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название курса"
    )
    description = models.TextField(
        verbose_name="Описание курса",
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Наш курс"
        verbose_name_plural = "Наши курсы"