from django.db import models

class Reserve (models.Model):
    name = models.CharField("Имя", max_length=128)
    phone = models.CharField("Номер телефона", max_length=128)
    guests = models.IntegerField("Гостей")
    time = models.TimeField("Время")

    def __str__(self):
        return self.name

    # class Meta:
    #     verbose_name = "Бронь"
    #     verbose_name_plural = "Бронь"
