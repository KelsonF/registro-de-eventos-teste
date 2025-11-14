from django.urls import path
from . import views

urlpatterns = [
  path('', views.AttendanceConfirmationView.as_view(), name='enter-access-code'),
  path('confirmar/<str:access_code>/', views.AttendanceConfirmationView.as_view(), name='attendance-confirm'),

  path('eventos', views.EventListView.as_view(), name='event-list'),
  path('evento/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
  path('evento/create/', views.EventCreateView.as_view(), name='event-create'),
  path('evento/<int:pk>/edit/', views.EventUpdateView.as_view(), name='event-update'),
  path('evento/<int:pk>/delete/', views.EventDeleteView.as_view(), name='event-delete'),
]