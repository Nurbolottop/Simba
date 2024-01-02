from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "название")
    description = models.CharField(max_length=155, verbose_name = "описание")
    image = models.ImageField(upload_to="image/", verbose_name="фото")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"