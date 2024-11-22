from django.contrib import admin
from main.models.brand import Brand
from main.models.category import Category
from main.models.galery import Galery
from main.models.group import GroupModel
from main.models.product import Product
from main.models.image import ImageField

class UserAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    pass

class ImageAdmin(admin.ModelAdmin):
    pass

class GroupAdmin(admin.ModelAdmin):
    pass

class GaleryAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class BrandAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
admin.site.register(ImageField, ImageAdmin)
admin.site.register(GroupModel, GroupAdmin)
admin.site.register(Galery, GaleryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)