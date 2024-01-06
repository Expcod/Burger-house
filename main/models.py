from django.db import models

class Choose(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    icon = models.ImageField()

class Choose_enjoy(models.Model):
    en_title = models.CharField(max_length=255)
    en_body = models.TextField()
    en_icon = models.ImageField()

class gallery(models.Model):
    image = models.ImageField()

class Order(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    people = models.IntegerField()
    is_active = models.BooleanField(True)

    def __str__(self):
        return f"Buyurtmachi: {self.name}"

    class Meta:
        verbose_name = "Buyurtmalar ro'yxati"
        ordering = ("-id",)
