"""project5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from Capstone import views as views



urlpatterns=[
    path("join/route/<int:route_id>", views.join_route, name="join_route"),
    path("leave/route/<int:route_id>", views.leave_route, name="leave_route"),

]
urlpatterns +=i18n_patterns(


    path('admin/', admin.site.urls),
    path("", include("Capstone.urls")),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='Capstone/password/password_reset.html'),
         name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="Capstone/password/password_reset_sent.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='Capstone/password/password_reset_form.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='Capstone/password/password_reset_complete.html'),
         name='password_reset_complete'),
    path('rosetta/', include('rosetta.urls'))


    #path('cookies/', include('cookie_consent.urls'))
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)