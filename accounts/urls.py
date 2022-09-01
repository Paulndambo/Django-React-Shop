from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", views.getRoutes),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("notes/", views.NoteGenericAPIView.as_view(), name="notes"),
    path("notes/<int:pk>/", views.NoteRetrieveUpdateDestroyAPIView.as_view(), name="notes-details"),
]