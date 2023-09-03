from django.contrib import admin
from home.models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category', 'image_tag']
    readonly_fields = ['image_tag', 'created_at']
    list_per_page = 20
    search_fields = ['title']
    list_filter = ['category']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'image_tag']
    readonly_fields = ['title', 'category', 'price', 'address', 'comment', 'first_name', 'last_name', 'phone_number',
                       'image_tag', 'ip', 'created_at']
    exclude = ['image']


class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image_tag']
    readonly_fields = ['image_tag']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Order, OrderAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(TelegramBot)
