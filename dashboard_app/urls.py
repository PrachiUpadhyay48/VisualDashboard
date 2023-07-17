"""demoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from dashboard_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.urls import include
from .views import DataAPIView

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('api/data/', views.api_data_view, name='api_data'),
    path('item/<int:item_id>/', views.item_detail_view, name='item_detail'),
    path('form/submit/', views.form_submit_view, name='form_submit'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/register/', views.register_view, name='register'),
    path('', include('dashboard_app.urls')),
    path('data/', DataAPIView.as_view(), name='data-api'),
]


# Add static file serving for development purposes
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
