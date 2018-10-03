from rest_framework import serializers

from products.models.exhibition_total_list import ExhibitionTotalList


class ExhibitionTotalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExhibitionTotalList
        fields = (
            'pk',
            'thumbnail',
            'title',
            'place',
            'duration',
        )
