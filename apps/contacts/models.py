from django.db import models

# Create your models here.
class Contact(models.Model):
    phone_number = models.CharField(max_length=15, verbose_name = "Телефонный номер")
    whatsapp = models.CharField(max_length=15, verbose_name = "Ватсап")
    inst = models.URLField(verbose_name = "инстаграм")
    email = models.EmailField(verbose_name = "Электронная почта")

    def __str__(self):
        return self.phone_number
    
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
    