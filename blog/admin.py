from django.contrib import admin
from .models import Category, Location, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('title', 'description')
    list_filter = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('name',)
    list_filter = ('is_published',)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'pub_date',
        'author',
        'category',
        'location',
        'is_published'
    )
    list_editable = ('is_published',)
    search_fields = ('title', 'text')
    list_filter = ('is_published', 'category', 'location', 'pub_date')
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
