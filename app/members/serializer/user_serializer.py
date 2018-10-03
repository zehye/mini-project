from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'img_profile',
            'first_name',
            'last_name',
            'phone_number',
            'address',
            'wish_list',
        )


