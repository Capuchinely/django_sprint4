# blog/forms.py
from django import forms
from .models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'pub_date', 'location', 'category', 'image')
        widgets = {
            'pub_date': forms.DateTimeInput(
                format='%Y-%m-%d %H:%M:%S',
                attrs={'type': 'datetime-local'}
            ),
            'text': forms.Textarea(attrs={'rows': 7}),
        }
        help_texts = {
            'pub_date': 'Формат: ГГГГ-ММ-ДД ЧЧ:ММ:СС',
            'image': 'Загрузите изображение для поста',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3}),
        }
        help_texts = {
            'text': 'Оставьте ваш комментарий',
        }