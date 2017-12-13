from django.conf.urls import url, include
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'vinyl/', include('apps.vinyl_app.urls')),
    url(r'^', include('apps.home_app.urls')),
    url(r'cd/', include('apps.cd_app.urls'))
]
