from django.db import models
from datetime import *

# Create your models here.

class Category(models.Model):
	"""docstring for ClassName"""
	name = models.CharField(max_length=255, verbose_name="Название категории" )
	alias = models.SlugField( verbose_name="Alias категории" )
	class Meta:
		verbose_name= "Категория"
		verbose_name_plural="Категории"
	def __str__(self):
		return 'Категория %s' % self.name
			
class Good(models.Model):
	"""docstring for ClassName"""
	name = models.CharField(max_length=255, verbose_name="Название товара" )
	category = models.ForeignKey(Category)
	price = models.IntegerField(default=0, verbose_name="Цена товара" )
	image = models.CharField(max_length=255, verbose_name="Ссылка на картинку" )
	number = models.IntegerField(default = 0,verbose_name="Количество товара")
	description = models.CharField(max_length=255,verbose_name="Описание товара")
	alias = models.SlugField( verbose_name="Alias товара" )
	class Meta:
		verbose_name= "Товар"
		verbose_name_plural="Товары"
	def __str__(self):
		return 'Товар %s' % self.name

