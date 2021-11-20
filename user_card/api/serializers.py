from rest_framework.serializers import ModelSerializer
from user_card.models import CardImage, UserCardData

class CardImageSerializers(ModelSerializer):
    class Meta:
        model = CardImage
        fields = [
            'id',
            'front_img',
            'back_img',
        ]

class UserCardDataSerializers(ModelSerializer):
    class Meta:
        model = UserCardData
        fields = [
            'id',
            'card_image',
            'id_number',
            'name',
            'nationality',
            'gender',
            'dob',
            'dox',
            'card_number',
        ]
