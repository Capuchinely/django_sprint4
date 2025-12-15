# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Главная страница (список постов)
    path('', views.IndexListView.as_view(), name='index'),
    
    # Страница поста
    path('posts/<int:post_id>/', views.PostDetailView.as_view(), name='post_detail'),
    
    # Страница категории
    path('category/<slug:category_slug>/', 
         views.CategoryPostsListView.as_view(), name='category_posts'),
    
    # Создание поста (только для авторизованных)
    path('posts/create/', views.PostCreateView.as_view(), name='post_create'),
    
    # Редактирование поста
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    
    # Удаление поста
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    
    # Комментарии
    path('posts/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('posts/<int:post_id>/edit_comment/<int:comment_id>/', 
         views.edit_comment, name='edit_comment'),
    path('posts/<int:post_id>/delete_comment/<int:comment_id>/', 
         views.delete_comment, name='delete_comment'),
]