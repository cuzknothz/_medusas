




from django.urls import path
from .views import goodluck


urlpatterns = [
    path('1/<str:pk>',goodluck)
]
