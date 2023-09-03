from django.db import models
from django.utils.safestring import mark_safe


class Category(models.Model):
    title = models.CharField(max_length=600)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kategoriyalar"
        verbose_name_plural = "Kategoriyalar"


class Product(models.Model):
    title = models.CharField(max_length=600)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    price = models.CharField(max_length=600)

    image = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe(
            f"<img src='{self.image.url}' style='width: 70px; height: 70px; object-fit: cover; object-position: center;' />")

    class Meta:
        verbose_name = "Maxsulotlar"
        verbose_name_plural = "Maxsulotlar"


class Order(models.Model):
    # product
    title = models.CharField(max_length=600)
    category = models.CharField(max_length=600)
    price = models.CharField(max_length=600)
    image = models.ImageField(upload_to='images/')

    # buyurtmachi
    first_name = models.CharField(max_length=600)
    last_name = models.CharField(max_length=600)
    phone_number = models.CharField(max_length=600)
    address = models.TextField()
    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe(
            f"<img src='{self.image.url}' style='width: 70px; height: 70px; object-fit: cover; object-position: center;' />")

    class Meta:
        verbose_name = "Buyurtmalar"
        verbose_name_plural = "Buyurtmalar"


class Banner(models.Model):
    category = models.CharField(max_length=600)
    title = models.CharField(max_length=600)
    price = models.CharField(max_length=600)
    image = models.ImageField(upload_to='images/')

    button_title = models.CharField(max_length=600)
    button_link = models.CharField(max_length=2000)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe(
            f"<img src='{self.image.url}' style='width: 70px; height: 70px; object-fit: cover; object-position: center;' />")

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banner"


class TelegramBot(models.Model):
    chat_id = models.CharField(max_length=600)
    bot_token = models.CharField(max_length=1000)

    def __str__(self):
        return self.chat_id

    class Meta:
        verbose_name = "Telegram Bot"
        verbose_name_plural = "Telegram Bot"
