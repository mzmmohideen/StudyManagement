from rest_framework import viewsets
from .models import Study
from .serializers import StudySerializer


class StudyViewSet(viewsets.ModelViewSet):
    """
    Provides all CRUD operations for the Study model via a REST API.
    """
    queryset = Study.objects.all()
    serializer_class = StudySerializer