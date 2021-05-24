from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import ProjectSerializer, MeasurementSerializer
from .models import Project, Measurement

class ProjectViewSet(ModelViewSet):
    """ViewSet для проекта."""
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class MeasurementViewSet(ModelViewSet):
    """ViewSet для измерения."""
    serializer_class = MeasurementSerializer
    queryset = Measurement.objects.all()
