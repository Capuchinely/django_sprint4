# blogicum/users/views.py
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.models import User

from .forms import CustomUserCreationForm


class CustomLoginView(LoginView):
    """Кастомный вход пользователя."""
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    """Кастомный выход пользователя."""
    template_name = 'users/logged_out.html'


class SignUpView(CreateView):
    """Регистрация нового пользователя."""
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('blog:index')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            'Вы успешно зарегистрировались! Теперь вы можете войти.'
        )
        return response


class ProfileDetailView(DetailView):
    """Просмотр профиля пользователя."""
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'profile_user'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем публикации пользователя (пример из блога)
        from blog.models import Post  # Импортируем здесь, чтобы избежать циклического импорта
        context['user_posts'] = Post.objects.filter(
            author=self.object
        ).order_by('-created_at')[:10]
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирование профиля пользователя."""
    model = User
    template_name = 'users/profile_edit.html'
    fields = ['first_name', 'last_name', 'username', 'email']
    success_url = reverse_lazy('users:profile_edit')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Профиль успешно обновлен!')
        return super().form_valid(form)


@login_required
def password_change(request):
    """Изменение пароля пользователя."""
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Ваш пароль был успешно изменен!')
            return redirect('users:profile', username=request.user.username)
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'users/password_change.html', {'form': form})


@login_required
def password_change_done(request):
    """Страница успешного изменения пароля."""
    return render(request, 'users/password_change_done.html')