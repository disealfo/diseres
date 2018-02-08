"""reservas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from app_authorization.views import index
from app_errors import views
from django.conf.urls import handler404


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', index, name='index'),
    url(r'^',include('app_authorization.urls',namespace='authorization')),
    url(r'^',include('app_establishment.urls',namespace='establishment')),
    url(r'^',include('app_people.urls',namespace='people')),
    url(r'^',include('app_products.urls',namespace='products')),
    url(r'^',include('app_reservations.urls',namespace='reservations')),
    url(r'^services/',include('app_services.urls',namespace='services')),
    #url(r'^listarServicios/',ServicioList.as_view(),name='servicio_listar')
]

handler404 = views.error_404