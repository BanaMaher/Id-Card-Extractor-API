
# from the same folder of challenges(.) imprt this app(module)
from django.urls import path
from rest_framework import views
from . import views 
#creates URLS config 
# urlpatterns = [
#     path("", views.index, name="index")
# ]
app_name = "user_card"   
urlpatterns = [
    # path("upload", DragDropView.as_view(), name="upload"),
    # path("savedupload", image_upload_view, name="saved-upload")
    path("upload", views.CreateProfileView.as_view(), name="upload")
]

#	Reverse for 'upload' not found. 'upload' is not a valid view function or pattern name.