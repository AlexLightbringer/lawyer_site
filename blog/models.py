from django.db import models


class Post(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=200, blank=False)
    content = models.TextField(verbose_name="Контент", blank=False)
    publish = models.BooleanField(verbose_name="Состояние", default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    

class Review(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя", blank=False)
    phone = models.CharField(max_length=10, verbose_name="Номер телефона", blank=False)
    content = models.TextField(max_length=300, verbose_name="Отзыв", blank=False)
    publish = models.BooleanField(verbose_name="Опубликовано", default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    grade = models.IntegerField(verbose_name="Оценка", default=5, blank=False)

    def __str__(self) -> str:
        return f"{self.grade}"