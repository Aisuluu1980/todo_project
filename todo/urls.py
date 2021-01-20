"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import homepage, third, add, update, delete, mark_todo, unmark_todo, close_todo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    # path('test', test, name='test'),
    path('third', third, name='third'),
    path('add', add, name='add'),
    path('update', update, name='update'),
    path('delete/<id>', delete, name='delete'),
    path('mark/<id>', mark_todo, name='mark_todo'),
    path('unmark/<id>', unmark_todo, name='unmark_todo'),
    path('closed/<id>', close_todo, name='close_todo'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
