from django.db import models

# from cke
# Create your models here.
class Style(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    descriptions = models.TextField(
        verbose_name = 'Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Стиль'
        verbose_name_plural = 'Стили'

class StyleInfo(models.Model):
    place_info = models.ForeignKey(Style,related_name = "place_info", on_delete  = models.CASCADE )
    image = models.ImageField(
        verbose_name = 'Фотография',
    )
    class Meta:
        unique_together = ('place_info', 'image')

class Glance(models.Model):
    name = models.CharField(
        max_length =255,
        verbose_name = 'Название'
    )
    descriptions = models.TextField(
        verbose_name = 'Описание'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория взгляда'
        verbose_name_plural = 'Категории взгляда'

class GlanceInfo(models.Model):
    place_info = models.ForeignKey(Glance,related_name = "glance_info", on_delete  = models.CASCADE )
    image = models.ImageField(
        verbose_name = 'Фотография сверху',
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    class Meta:
        unique_together = ('place_info', 'image')
  

class Discount(models.Model):
    image = models.ImageField(
        upload_to='image_goods',
        verbose_name='Фотография'
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Заголовок'
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Название'
    )
    descriptions = models.TextField(
        verbose_name = 'Описание'
    )
    now_price = models.CharField(
        max_length = 255,
        verbose_name = 'Цена сейчас'
    )
    before_price = models.CharField(
        max_length = 255,
        verbose_name = 'Цена раньше'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'


class Collection(models.Model):
    descriptions = models.TextField(
        verbose_name = 'Описание'
    )
    
    def __str__(self):
        return self.descriptions
    
    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'


class CollectionInline(models.Model):
    place_info = models.ForeignKey(Collection,related_name = "collection_info", on_delete  = models.CASCADE )
    image = models.ImageField(
        verbose_name = 'Фотография сверху',
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    price = models.CharField(
        max_length = 255,
        verbose_name = 'Цена'
    )
    size = models.CharField(
        max_length = 255,
        verbose_name = 'Размеры'
    )
    class Meta:
        unique_together = ('place_info', 'image')

class Testimonials(models.Model):
    mini_descriptions = models.TextField(
        max_length =255,
        verbose_name = 'Мини описание'
    )
    def __str__(self):
        return self.mini_descriptions
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = 'Отзывы'
    

class TestimonialsInline(models.Model):
    place_info = models.ForeignKey(Testimonials,related_name = "testimonials_info", on_delete  = models.CASCADE )
    image = models.ImageField(
        upload_to='testimonials/image',
        verbose_name='Фото клиентов'
    )
    testimonial = models.TextField(
        verbose_name = 'Отзыв'
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя клиента'
    )
    class Meta:
        unique_together = ('place_info', 'image')
    
class Trends(models.Model):
    first_descrip = models.TextField(
        verbose_name = 'Главное описание'
    )
    image = models.ImageField(
        upload_to='trends_image',
        verbose_name='Большое фото'
    )
    goods = models.ImageField(
        upload_to='goods/trend/image',
        verbose_name='Фото товара'
    )
    card_image = models.ImageField(
        upload_to='card_image',
        verbose_name='Фото внутри карточки'
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название товара'
    )
    descriptions = models.TextField(
        verbose_name = 'Описание товара'
    )
    now_price = models.CharField(
        max_length = 255,
        verbose_name = 'Цена сейчас'
    )
    before_price = models.CharField(
        max_length = 255,
        verbose_name = 'Цена раньше'
    )
    size = models.CharField(
        max_length = 255,
        verbose_name = 'Размеры'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Товар Тренд'
        verbose_name_plural = 'Товары Тренды'

class Partner(models.Model):
    image = models.ImageField(
        upload_to='partner_image',
        verbose_name='Фотография '
    )
    class Meta:
        verbose_name = 'Парнер'
        verbose_name_plural ='Партнеры'


class Art(models.Model):
    part = models.CharField(
        max_length = 255,
        verbose_name = 'Название части'
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя'
    )
    descriptions = models.TextField(
        verbose_name = 'Описание товара'
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Отдел товаров'
        verbose_name_plural = 'Отделы товаров'



