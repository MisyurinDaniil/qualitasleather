"""qualitasleather URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from appCMS.views import index_page, category_page, product_page, contacts_page
from appOrders.views import makeorder


# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    path('', index_page),
    path('category/<int:idProductCategory>/', category_page),
    path('product/<int:idProductItem>/', product_page),
    path('contacts/', contacts_page),
    path('makeorder/', makeorder),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)