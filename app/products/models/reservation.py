from django.db import models

from products.models.exhibition import Exhibition


class ExhibitionReservation(models.Model):
    """
    전시 예약
    """
    RESERVATION_TYPE = (
        ('양일권', ''),
        ('일일권', ''),
    )
    reservation = models.ForeignKey(
        Exhibition,
        on_delete=models.CASCADE,
    )
