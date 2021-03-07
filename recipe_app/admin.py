from django.contrib import admin
from .models import Items
# Register your models here.


class ItemsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Items, ItemsAdmin)
