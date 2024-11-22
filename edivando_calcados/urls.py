"""
URL configuration for edivando_calcados project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from main.views.brand_vw import BrandViewset
from main.views.category_vw import CategoryViewset
from main.views.galery_vw import GaleryViewset
from main.views.group_vw import GroupViewset
from main.views.image_vw import ImageViewset
from main.views.product_vw import ProductViewset
from main.views.user_vw import UserViewset


router = DefaultRouter()

router.register(r'user', UserViewset)
router.register(r'products', ProductViewset)
router.register(r'image', ImageViewset)
router.register(r'group', GroupViewset)
router.register(r'galery', GaleryViewset)
router.register(r'category', CategoryViewset)
router.register(r'brand', BrandViewset)
urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    path(r"auth/", include("djoser.urls.authtoken")),
    path(r"auth/", include("djoser.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
