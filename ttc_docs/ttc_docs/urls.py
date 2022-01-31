from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ru/', include(('web_docs.urls', 'web_docs'), namespace='ru')),
    path('ua/', include(('web_docs_ua.urls', 'web_docs_ua'), namespace='ua')),
]
