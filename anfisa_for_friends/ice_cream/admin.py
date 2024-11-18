from django.contrib import admin
from .models import Category, IceCream, Topping, Wrapper
# from .models import Category
# from .models import Topping
# from .models import Wrapper
# from .models import IceCream


# admin.site.register(Category)
admin.site.register(Topping)
admin.site.register(Wrapper)
# admin.site.register(IceCream)

class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )    
    search_fields = ('title',) 
    list_filter = ('category',)
    list_display_links = ('title',)
    empty_value_display = 'Не задано'
    filter_horizontal = ('toppings',)

# Регистрируем кастомное представление админ-зоны
admin.site.register(IceCream, IceCreamAdmin)

# Подготавливаем модель IceCream для вставки на страницу другой модели.
class IceCreamInline(admin.StackedInline):
# class IceCreamInline(admin.TabularInline):
    model = IceCream
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',        
    )

admin.site.register(Category, CategoryAdmin) 