from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView, 
    CreateAPIView)

from user_card.models import CardImage, UserCardData
from .serializers import CardImageSerializers, UserCardDataSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
#create api : user will enter new field
class CreateUserImageAPIView(CreateAPIView):
    queryset = CardImage.objects.all()
    # queryset = CardImage.objects.all().values('id','front_img', 'back_img')
    serializer_class = CardImageSerializers

    # def create(self, request, *args, **kwargs):
    #     userimage_data = request.data
    #     #creating new object 
    #     new_usercardata = UserCardData.objects.create(
    #         id_number=userimage_data["id_number"],
    #         name=userimage_data["name"],
    #         nationality=userimage_data["nationality"],
    #         gender=userimage_data["gender"],
    #         dob=userimage_data["dob"],
    #         dox=userimage_data["dox"],
    #         card_number=userimage_data["card_number"]
    #     )
    #     new_usercardata.save()

    # #creating a new object of card image model
    #     new_cardimage = CardImage.objects.create(
    #         front_img=userimage_data["front_img"],
    #         back_img=userimage_data["back_img"],
    #         usercarddata=new_usercardata
    #     )
    #     new_usercardata.save()

    #     serializer = CardImageSerializers(new_cardimage)

    #     return Response(serializer)


#get api for card image
class GetUserImageListAPIView(ListAPIView):
    queryset = CardImage.objects.all()
    serializer_class = CardImageSerializers

# Retrieve detail data about a user using ID=pk
class RetrieveDetailForUserImageAPIView(RetrieveAPIView):
    queryset = CardImage.objects.all()
    serializer_class = CardImageSerializers

#get user card full data 
class GetUserDataImageListAPIView(ListAPIView):
    queryset = UserCardData.objects.all()
    serializer_class = UserCardDataSerializers
