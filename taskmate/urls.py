
from django.contrib import admin
from django.urls import path, include
from taskmanager import views as task_views
from users_app import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include("users_app.urls")),
    path('', task_views.index, name='index'),
    path('task/', include('taskmanager.urls')),
    path('about', task_views.about, name='about'),
    path('contact', task_views.contact, name='contact'),
]
