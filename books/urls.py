from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import BookCreateView, BookListView, BookUpdateView, BookDeleteView, AdminLoginView, \
    CustomTokenObtainPairView, get_csrf_token, AdminSignupView

urlpatterns = [
    path('admin/signup/', AdminSignupView.as_view(), name='admin-signup'),
    path('admin/login/', AdminLoginView.as_view(), name='admin-login'),

    # ✅ Add JWT Token Endpoints
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login & get tokens
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh access token
    path("csrf/", get_csrf_token, name="csrf_token"),

    # Book Endpoints
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]
