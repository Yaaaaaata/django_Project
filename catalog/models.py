from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    """name: CharField с максимальной длиной 100 символов, для хранения наименования категории."""
    description = models.TextField(max_length=512, verbose_name='описание')
    """description: TextField с максимальной длиной 512 символов, для хранения описания категории."""

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    """name: CharField с максимальной длиной 100 символов, для хранения наименования продукта."""
    description = models.TextField(max_length=512, verbose_name='описание')
    """description: TextField с максимальной длиной 512 символов, для хранения описания категории."""
    image = models.ImageField(upload_to='products/', verbose_name='изображение (превью)')
    """image: ImageField для хранения изображения продукта. 
    Параметр upload_to указывает папку, в которую будут загружаться изображения."""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    """category: ForeignKey для связи с моделью Category. 
    При удалении категории, все продукты с этой категорией также будут удалены."""
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='цена за покупку')
    """price: DecimalField для хранения цены за покупку продукта. 
    Параметры max_digits и decimal_places определяют точность числа."""
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    """created_at: DateTimeField с параметром auto_now_add=True, 
    который будет автоматически устанавливать текущую дату и время при создании записи."""
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')
    """updated_at: DateTimeField с параметром auto_now=True, 
    который будет автоматически обновлять текущую дату и время при каждом сохранении записи."""

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
