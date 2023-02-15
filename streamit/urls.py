from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from api.views import home, activate_account, reset_password_confirm, reset_password_email

admin.site.site_header  =  "TSL Nigeria Administration"  
admin.site.site_title  =  "TSL Nigeria"
admin.site.index_title  =  "DASHBOARD"

urlpatterns = [
    path('', home, name='home'),
    path('activate/<str:uid>/<str:token>/', activate_account, name="activate-account"),
    # password/reset/confirm/{uid}/{token}
    path('password/reset/confirm/<str:uid>/<str:token>/', reset_password_confirm, name="reset_password_confirm"),
    path('reset/password/email/', reset_password_email, name="change_password"),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('user/', include('users.urls')),
    

    # Djoser
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls.authtoken')),

    # Oauth for social logins
    path('oauth/', include('drf_social_oauth2.urls', namespace='drf')),
    
    path('social/auth/', include('djoser.social.urls')),
    
    
    # Dummy Account for social test
    path('accounts/', include('accounts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


