from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('artists/', include('artists.urls')),
                  path('albums/', include('albums.urls')),
                  path('users/', include('users.urls')),
                  path('authentication/', include('authentication.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += path('api-auth/', include('rest_framework.urls')),
