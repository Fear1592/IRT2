from django.db import models
from django.conf import settings


class CategoryMakers(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название категории')

    class Meta:
        ordering = ['id']
        verbose_name = "Категория производителей"
        verbose_name_plural = "Категории производителей"

    def __str__(self):
        return self.name


class Produced(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец поста')
    name = models.CharField(max_length=155, verbose_name='Название товара')
    article_number = models.CharField(max_length=50, verbose_name='Артикул')
    specifications = models.TextField(verbose_name='Характеристики', blank=True, null=True)
    equipment = models.TextField(verbose_name='Комплектация', blank=True, null=True)
    category = models.ForeignKey(CategoryMakers,
                                 verbose_name='Категория товара',
                                 on_delete=models.CASCADE)
    price = models.PositiveIntegerField(verbose_name='Цена товара')
    is_published = models.BooleanField(default=False, verbose_name='Опбуликовано')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def current_view(self):
        return self.view.hits

    def __str__(self):
        return str(self.name)


class Images(models.Model):
    produced = models.ForeignKey(Produced, on_delete=models.CASCADE, verbose_name='Услуга', related_name='images')
    image = models.ImageField(upload_to='image/', verbose_name='Общие изображения услуги')

    class Meta:
        ordering = ['id']
        verbose_name = "Изображения товара"
        verbose_name_plural = "Изображения товаров"

    def __str__(self):
        return str(self.image)
