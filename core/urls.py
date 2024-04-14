
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('admin_app.urls')),
    path('', include('building_app.urls')),
    path('', include('handler_app.urls')),
    path('', include('employee_app.urls', namespace='employee_app')),
    path('', include("apps.authentication.urls")), # Auth routes - login / register
    path('', include("apps.home.urls"))             # UI Kits Html files
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
