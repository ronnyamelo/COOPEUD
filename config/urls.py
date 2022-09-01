"""config URL Configuration

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
from django.urls import path, include
from rest_framework import routers
from loanrequest import views
from coopeud import views as web_views

router = routers.DefaultRouter()
# router.register(r'api/solicitudes', views.LoanRequestViewSet)
router.register(r'', views.LoanRequestViewSet)

urlpatterns = [
    path('', web_views.index, name='index'),
    path('contacto/', web_views.contact, name='contact'),
    path('ubicacion/', web_views.location, name = 'location'),
    path(r'solicitud_prestamo/', web_views.formulario, name='form'),
    path(r'api/solicitudes/', views.LoanRequestCreateViewSet.as_view(), name='test'),
    path('admin/solicitudes/', include(router.urls)),
    path(r'solicitud_prestamo/2/', web_views.formulario2, name='form2'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='login'),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('nosotros/', web_views.history, name = 'history'),
    # path("accounts/", include("django.contrib.auth.urls")),
    # path("admin/", admin.site.urls),
    # path('admin/', views.TestViewSet.as_view({'get': 'list'}), name='test'),
    # path('test/', views.test, name='token')


]
