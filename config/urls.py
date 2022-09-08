from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from loanrequest import views
from coopeud import views as web_views

router = routers.DefaultRouter()
router.register(r'', views.LoanRequestViewSet)

urlpatterns = [
    path('', web_views.index, name='index'),
    path('contacto/', web_views.contact, name='contact'),
    path('ubicacion/', web_views.location, name = 'location'),
    path(r'solicitud_prestamo/', web_views.formulario, name='form'),
    path(r'api/solicitudes/', views.LoanRequestCreateViewSet.as_view(), name='test'),
    path('admin/solicitudes/', include(router.urls)),
    path(r'solicitud_prestamo/2/', web_views.formulario2, name='form2'),
    # path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('nosotros/', web_views.history, name = 'history'),
    path('crear_solicitud/', web_views.handle_loan_request, name="handle_loan_request"),
    #  path("accounts/", include("django.contrib.auth.urls")),
    # path("a/", admin.site.urls),
    path('oauth2/', include('django_auth_adfs.urls')),
]
