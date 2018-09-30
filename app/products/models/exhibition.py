from django.db import models


class Exhibition(models.Model):
    """
    각 전시, 공연들의 세부 정보
    """
    # 전시 이름
    title = models.CharField(max_length=20)

    # 전시 간략 소개
    description = models.TextField()

    # 리뷰
    photo_review = models.ImageField(blank=True)
    text_review = models.TextField(blank=True)

    # 상세정보
    photo_event = models.ImageField(blank=True)
    text_event = models.TextField(blank=True)

    # 위도
    address_latitude = models.DecimalField(
        verbose_name='Google MAP API 위도',
        decimal_places=14,
        max_digits=16,
        blank=True,
    )

    # 경도
    address_longitude = models.DecimalField(
        verbose_name='Google MAP API 경도',
        decimal_places=14,
        max_digits=17,
        blank=True,
    )

