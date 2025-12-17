from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView
from .forms import CustomUserCreationForm, ProfileUpdateForm
from ice_cream.models import IceCream  # предположим, что у вас есть модель IceCream
from django.core.paginator import Paginator


def registration(request):
    """Регистрация нового пользователя"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage:index')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'users/registration.html', {'form': form})


class UserProfileView(DetailView):
    """Страница профиля пользователя"""
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'profile_user'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        
        # Получаем публикации пользователя с пагинацией
        posts = IceCream.objects.filter(
            is_published=True,
            owner=user
        ).order_by('-created_at')
        
        paginator = Paginator(posts, 10)  # 10 постов на страницу
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context['page_obj'] = page_obj
        context['is_owner'] = self.request.user == user
        return context


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Редактирование профиля"""
    model = User
    form_class = ProfileUpdateForm
    template_name = 'users/profile_edit.html'
    
    def get_success_url(self):
        return reverse_lazy('users:profile', kwargs={'username': self.object.username})
    
    def test_func(self):
        user = self.get_object()
        return self.request.user == user