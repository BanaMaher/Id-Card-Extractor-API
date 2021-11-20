from django.contrib import admin
from .models import CardImage,UserCardData
# Register your models here.
class CardImageAdmin(admin.ModelAdmin):
    list_display = ("id", "front_img", "back_img",)

class UserCardDataAdmin(admin.ModelAdmin):
    list_display = ("id", "id_number", "name", "nationaliy", "gender", "dob", "dox", "card_number")

admin.site.register(CardImage, CardImageAdmin)

admin.site.register(UserCardData, UserCardDataAdmin)

