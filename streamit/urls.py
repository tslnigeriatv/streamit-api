from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from api.views import home, activate_account

admin.site.site_header  =  "TSL Nigeria Administration"  
admin.site.site_title  =  "TSL Nigeria"
admin.site.index_title  =  "DASHBOARD"

urlpatterns = [
    path('', home, name='home'),
    path('activate/<str:uid>/<str:token>/', activate_account, name="activate-account"),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('user/', include('users.urls')),
    

    # Djoser
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls.authtoken')),

    # Oauth for social logins
    path('oauth/', include('drf_social_oauth2.urls', namespace='drf')),
    
    path('oauth/', include('djoser.social.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


