from rest_framework.routers import DefaultRouter
from .viewsets import StudyViewSet
from django.urls import path
from . import views # Assuming you named the functions above

router = DefaultRouter()
router.register(r'api/studies', StudyViewSet, basename='study') # Added basename for clarity

# Define the urlpatterns list once, combining all paths.
urlpatterns = [
    # Frontend HTML pages (relative to /studies/ due to main project include)
    path('', views.main_view_page, name='main_view_page'),
    path('add/', views.add_study_page, name='add_study_page'),
    path('edit/<int:pk>/', views.edit_study_page, name='edit_study_page'),
    path('view/<int:pk>/', views.view_study_page, name='view_study_page'),
] 

# Append the DRF router URLs to the list of frontend URLs
urlpatterns += router.urls
