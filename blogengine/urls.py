from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from filebrowser.sites import site


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/filebrowser/', site.urls),
    path('accounts/', include('allauth.urls')),
    path('tinymce/', include('tinymce.urls')), 
    path('', include('core.urls'))
]

# \
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
