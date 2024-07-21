from django.db import models
from django.core.validators import MaxValueValidator,  MinValueValidator


class Task(models.Model):
    value = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    name = models.CharField('Имя пользователя', max_length=50)
    text = models.TextField('Комментарий')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'


class Comment(models.Model):
    keys = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    autor = models.CharField('Имя пользователя', max_length=50)
    comment = models.TextField('Комментарий')

    def __str__(self):
        return self.autor

    class Meta:
        verbose_name = "комментарии к отзывам"
        verbose_name_plural = 'комментарии к отзывам'
