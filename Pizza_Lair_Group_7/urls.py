"""
URL configuration for Pizza_Lair_Group_7 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from . import views

#################################################
# https://www.youtube.com/watch?v=NgHvfxkEKhQ
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib.auth.models import User
# from django_otp.plugins.otp_totp.models import TOTPDevice
# from django_otp.admin import OTPAdminSite
# from main import models as main
# class MediaAdmin(admin.ModelAdmin):
#     list_display = ("id", "url")
# class OTPAdmin(OTPAdminSite):
#     pass
# admin_site = OTPAdmin(name="OTPAdmin")
# admin_site.register(User)
# admin_site.register(TOTPDevice)
# admin_site.register(main.Media, MediaAdmin)
#################################################

urlpatterns = [
    # path("django_admin/", admin.site.urls),               # youtube
    path("admin/", admin.site.urls),
    # path("", include('main.urls', namespace='main')),     # youtube
    path("", include("product.urls")),
    path("order/", include("product.urls")),
    path("user/", include("user.urls")),
    path("checkout/", include("checkout.urls"))
]

# Exception and Error Handling
handler400 = views.handler400
handler403 = views.handler403
handler404 = views.handler404
handler500 = views.handler500
