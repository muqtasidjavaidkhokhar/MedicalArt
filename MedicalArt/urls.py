from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
import home.views
from django.views.generic import TemplateView

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', home.views.index, name='index'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)