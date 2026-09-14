from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clear-history/', views.clear_history, name='clear_history'), # Added clear endpoint
    # ADD THESE TWO LINES:
    path('toggle-status/<int:log_id>/', views.toggle_status, name='toggle_status'),
    path('retrain-model/', views.retrain_model, name='retrain_model'),
]
