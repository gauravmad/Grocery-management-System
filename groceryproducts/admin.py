from django.contrib import admin
from groceryproducts.models import category, Grocery, Product


# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    list_display = ('category_img','category_title')
    
admin.site.register(category,categoryAdmin)  

class GroceryAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantity')

admin.site.register(Grocery,GroceryAdmin)

class productAdmin(admin.ModelAdmin):
    list_display = ('product_img','product_title','product_price')

admin.site.register(Product, productAdmin)    