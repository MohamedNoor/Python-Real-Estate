from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#import from django library

urlpatterns = [
#added path to url
    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('listings/', include('listings.urls')),
    path('contacts/', include('contacts.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
