from django_filters import rest_framework as filters

from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    status = filters.ModelMultipleChoiceFilter(
        to_field_name="status",
        queryset=Advertisement.objects.all()
    )
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ('status', 'created_at', )
