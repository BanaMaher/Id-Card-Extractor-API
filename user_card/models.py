from django.db import models
from PIL import Image
from django.db.models.fields.files import ImageField
# Create your models here.

class CardImage(models.Model):
    front_img = models.ImageField(upload_to="images")
    back_img = models.ImageField(upload_to="images")
    
    def __str__(self):
        return f"{self.id} {self.front_img} {self.back_img}"

    # def save(self,*args, **kwargs ):
    #     #open Image
    #     pil_img = Image.open(self.front_img)

    class Meta:
        verbose_name_plural = "CardImage"

class UserCardData(models.Model):
    usercarddata = models.OneToOneField(CardImage, on_delete = models.CASCADE, null=True)
    id_number = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    nationaliy = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    dox = models.CharField(max_length=100)
    card_number = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}{self.id_number}{self.name}{self.nationaliy}{self.gender}{self.dob}{self.dox}{self.card_number}"

    class Meta:
        verbose_name_plural = "UserCardData"