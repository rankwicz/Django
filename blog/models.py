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
    title = models.CharField('Название статьи',max_length=100, unique=True)
    text = models.TextField('Основной текст статьи')
    date = models.DateTimeField('Дата', default=timezone.now)
    autor = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    
    views = models.IntegerField('Просмотры', default=1)
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'XLarge'),
    )

    shop_sizes = models.CharField('Размер статьи', max_length=2, choices=sizes, default='S')
#после того как создали таблицу нужно создать миграции 
# python3 manage.py makemigrations
# данная команда лишь позволяет создать миграции
#проводим миграцию python3 manage.py migrate
#дальше нужно зарегистрировать таблицу в панеле администратора admin.py
    #добавляем магическую функцию 
    # после которой название статьи будет нормальным
    def __str__(self):
        return self.title
            #также можно добавить форматированноу строку 
            # например return f'Новость {self.title}' 
            # что будет выводить 'Новость: (название)'

    #Переименуем название. Django дописывает букву S (Newss)
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'