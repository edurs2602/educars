from django.contrib import admin
from .models import Vehicle, Item


class ItemInline(admin.TabularInline):
    model = Vehicle.items.through
    extra = 1


class VehicleAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
    exclude = ('items',)


admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Item)
