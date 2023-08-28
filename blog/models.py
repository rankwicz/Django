from django.db import models
#чтобы брать текущее время для колоник ДАТА, нужно подключить
from django.utils import timezone
#привязать статью к определённому пользователю
from django.contrib.auth.models import User

# Create your models here.
# файл для работы с базой данных
# эти таблицы можно редактировать через панель администратора

#создаём новую табличку. название класса любое
class News(models.Model):
    title = models.CharField('Название статьи',max_length=100)
    text = models.TextField('Основной текст статьи')
    date = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=None)