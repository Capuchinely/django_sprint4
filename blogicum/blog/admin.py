from django.contrib import admin
from .models import Category, Location, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'created_at')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['title'].label = 'Заголовок'
        form.base_fields['description'].label = 'Описание'
        form.base_fields['slug'].label = 'Идентификатор'
        form.base_fields['slug'].help_text = (
            'Идентификатор страницы для URL; разрешены символы латиницы, '
            'цифры, дефис и подчёркивание.'
        )
        form.base_fields['is_published'].label = 'Опубликовано'
        form.base_fields['is_published'].help_text = (
            'Снимите галочку, чтобы скрыть публикацию.'
        )
        form.base_fields['created_at'].label = 'Добавлено'
        return form


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    list_filter = ('is_published', 'created_at')
    search_fields = ('name',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['name'].label = 'Название места'
        form.base_fields['is_published'].label = 'Опубликовано'
        form.base_fields['is_published'].help_text = (
            'Снимите галочку, чтобы скрыть публикацию.'
        )
        form.base_fields['created_at'].label = 'Добавлено'
        return form


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'author', 'category',
                    'location', 'is_published', 'created_at')
    list_filter = ('is_published', 'category', 'location', 'pub_date')
    search_fields = ('title', 'text')
    date_hierarchy = 'pub_date'
    raw_id_fields = ('author',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['title'].label = 'Заголовок'
        form.base_fields['text'].label = 'Текст'
        form.base_fields['pub_date'].label = 'Дата и время публикации'
        form.base_fields['pub_date'].help_text = (
            'Если установить дату и время в будущем — '
            'можно делать отложенные публикации.'
        )
        form.base_fields['author'].label = 'Автор публикации'
        form.base_fields['category'].label = 'Категория'
        form.base_fields['location'].label = 'Местоположение'
        form.base_fields['is_published'].label = 'Опубликовано'
        form.base_fields['is_published'].help_text = (
            'Снимите галочку, чтобы скрыть публикацию.'
        )
        form.base_fields['created_at'].label = 'Добавлено'
        return form
