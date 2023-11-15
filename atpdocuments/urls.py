from django.urls import path
from .views import ATPDocumentListCreateView, ATPDocumentDetailsListCreateView
from .views import UserRegistrationView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('api/atp-documents/', ATPDocumentListCreateView.as_view(), name='atp-document-list'),
    path('api/atp-documents/<int:pk>/', ATPDocumentListCreateView.as_view(), name='atp-document-detail'),
    path('api/atp-document-details/', ATPDocumentDetailsListCreateView.as_view(), name='atp-document-details-list'),
    path('api/atp-document-details/<int:pk>/', ATPDocumentDetailsListCreateView.as_view(), name='atp-document-detail'),
    path('api/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('api/login/', ObtainAuthToken.as_view(), name='login'),
]
