from django.db import models
from django.conf import settings


class CategoryShop(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название категории')

    class Meta:
        ordering = ['id']
        verbose_name = "Категория магазинов"
        verbose_name_plural = "Категории магазинов"

    def __str__(self):
        return self.name


class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец поста')
    name = models.CharField(max_length=155, verbose_name='Название товара')
    choice_cat = models.CharField(max_length=155, verbose_name='Название подкатегорий',
                                  blank=True, null=True)
    specifications = models.TextField(verbose_name='Характеристики', blank=True, null=True)
    equipment = models.TextField(verbose_name='Комплектация', blank=True, null=True)
    category = models.ForeignKey(CategoryShop,
                                 verbose_name='Категория товара',
                                 on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False, verbose_name='Опбуликовано')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='images')
    image = models.ImageField(upload_to='product/', verbose_name='Общие изображения товаров')

    class Meta:
        ordering = ['id']
        verbose_name = "Изображения товара"
        verbose_name_plural = "Изображения товаров"

    def __str__(self):
        return str(self.image)


class Choices(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='choices')
    name = models.CharField(max_length=150, verbose_name='Имя типа товара цвет/вкус')
    article_number = models.CharField(max_length=50, verbose_name='Артикул')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')
    count = models.PositiveIntegerField(default=0, verbose_name='Колличество товара')
    image = models.ImageField(upload_to='choices/', verbose_name='Изображение категории')
    price = models.PositiveIntegerField(verbose_name='Цена товара')

    class Meta:
        ordering = ['-id']
        verbose_name = "Разновидность товара"
        verbose_name_plural = "Разновидности товаров"

    def __str__(self):
        return self.name
