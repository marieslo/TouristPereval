from django.contrib import admin
from django.urls import path, include

from pereval.views import PerevalCreateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('create/', PerevalCreateView.as_view()),
]