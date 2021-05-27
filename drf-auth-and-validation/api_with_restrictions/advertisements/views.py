from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from advertisements.filters import AdvertisementFilter


class UserIsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["destroy", "update", "partial_update"]:
            return [IsAuthenticated(), UserIsOwner()]
        elif self.action == "create":
            return [IsAuthenticated()]
        return []
