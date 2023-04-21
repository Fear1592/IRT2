from django.db import models
from django.conf import settings


class CategoryService(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название категории')

    class Meta:
        ordering = ['id']
        verbose_name = "Категория услуг"
        verbose_name_plural = "Категории услуг"

    def __str__(self):
        return self.name


class Service(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец поста')
    name = models.CharField(max_length=155, verbose_name='Название товара')
    specifications = models.TextField(verbose_name='Характеристики', blank=True, null=True)
    equipment = models.TextField(verbose_name='Комплектация', blank=True, null=True)
    category = models.ForeignKey(CategoryService,
                                 verbose_name='Категория товара',
                                 on_delete=models.CASCADE)
    price = models.PositiveIntegerField(verbose_name='Цена товара')
    is_published = models.BooleanField(default=False, verbose_name='Опбуликовано')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name


class Images(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Услуга', related_name='images')
    image = models.ImageField(upload_to='service/', verbose_name='Общие изображения услуги')

    class Meta:
        ordering = ['id']
        verbose_name = "Изображения услуги"
        verbose_name_plural = "Изображения услуг"

    def __str__(self):
        return self.image
