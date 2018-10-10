from django.db import models

from products.models import ExhibitionTotalList
from .. import crawler_detail


class Exhibition(models.Model):
    """
    각 전시, 공연들의 세부 정보
    """
    title = models.ForeignKey(
        ExhibitionTotalList,
        on_delete=models.CASCADE,
    )
    sm_title = models.CharField(max_length=100)
    description = models.TextField()
    photo_desc = models.ImageField(blank=True)
    text_desc = models.TextField(blank=True)
    address = models.ImageField(upload_to='exhibition_detail_map', blank=True)
    no = models.IntegerField(blank=True)

    def get_exhibition_crawler(self):
        exhibition = crawler_detail.GetExhibitionDetail().get_exhibition_detail()
        return exhibition

    def create_exhibition(self):
        pass


class ExhibitionReview(models.Model):
    account = models.CharField(max_length=30)
    score = models.CharField(max_length=10)
    body = models.TextField(blank=True)
    date = models.CharField(max_length=20)


