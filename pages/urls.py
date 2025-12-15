# pages/urls.py
from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.AboutView.as_view(), name='about'),
    # URL для тестирования страниц ошибок (для разработки)
    path('403/', views.csrf_failure, name='403'),  # ← Имя функции: csrf_failure
    path('404/', views.page_not_found, name='404'), # ← Имя функции: page_not_found
    path('500/', views.server_error, name='500'),   # ← Имя функции: server_error
]