# Register your models here.
from django.contrib import admin
# импортируем таблицу для регистрации
from .models import News
#регистрируем
admin.site.register(News)



