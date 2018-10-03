from rest_framework.views import APIView
from rest_framework.response import Response

from products.models.exhibition_total_list import ExhibitionTotalList
from products.serializer import ExhibitionTotalListSerializer


class ExhibitionList(APIView):
    def get(self, request, format=None):
        exhibitions = ExhibitionTotalList.objects.all()
        serializer = ExhibitionTotalListSerializer(exhibitions, many=True)
        return Response(serializer.data)
