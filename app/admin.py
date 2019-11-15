from django.contrib import admin
from app.models import DogProduct, Purchase, DogTag


class DogProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(DogProduct, DogProductAdmin)


class PurchaseAdmin(admin.ModelAdmin):
    pass


admin.site.register(Purchase, PurchaseAdmin)

class DogTagAdmin(admin.ModelAdmin):
    pass


admin.site.register(DogTag, DogTagAdmin)
