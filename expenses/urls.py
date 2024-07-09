from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from expenses import settings
from app import views, views_auth


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register/', views_auth.registration, name='register'),
    path('login/', views_auth.login_view, name='login'),
    path('logout/', views_auth.logout_view, name='logout'),
    path('account/', views.account, name='account'),
    path('account/<str:transaction_type>/', views.account, name='account'),  # Добавляем новый путь
    path('create/', views.create_view, name='create'),
    path('delete/<int:transaction_id>', views.delete_view, name='delete'),
    path('edit/<int:transaction_id>', views.edit_view, name='edit'),
    path('add10', views.add10, name='add10'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



