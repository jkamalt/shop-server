from django.contrib import admin

from products.models import ProductCategory, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', ('price', 'quantity'), 'category', 'image')
    ordering = ('name',)
    search_fields = ('name',)


class ProductInline(admin.TabularInline):
    model = Product
    fields = ('name', 'quantity', 'price')
    extra = 0


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    inlines = (ProductInline,)
    list_display = ('name', 'description')
    ordering = ('name',)
    search_fields = ('name',)
