from django.contrib import admin

# Register your models here.


from .models import Element, Category, TypeElement



class TypeAdmin(admin.ModelAdmin):
    list_display =("id","title")

class CategoryAdmin(admin.ModelAdmin):
    list_display =("id","title")

class ElementAdmin(admin.ModelAdmin):
    list_display =("id","title")

admin.site.register(TypeElement,TypeAdmin)
admin.site.register(Element,ElementAdmin)
admin.site.register(Category,CategoryAdmin)