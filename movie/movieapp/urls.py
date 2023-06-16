from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include

from movieapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index.html'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/',views.add_movie,name="add_movie"),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]

app_name='movieapp'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
