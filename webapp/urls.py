from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
import webapp

# ---



urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
