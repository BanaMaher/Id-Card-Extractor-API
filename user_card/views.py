from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from .forms import CardImageForm
from django.core.files.storage import FileSystemStorage
from .models import CardImage
from .forms import CardImageForm

#rendering the page in website
# class DragDropView(TemplateView):
#     template_name = "user_card/index.html"

#creating a new function to save the uploaded image in db
# def file_upload_view(request):
#     if request.method ==
#     return HttpResponse('upload')

# class CreateProfileView(CreateView):
#     template_name = "user_card/index.html"
#     model = CardImage
#     fields = "__all__"
#     success_url = "/profiles"

# def image_upload_view(request):
#     """Process images uploaded by users"""
#     if request.method == 'POST':
#         form = CardImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # Get the current instance object to display in the template
#             img_obj = form.instance
#             return render(request, "index.html", {'form': form, 'img_obj': img_obj})
#     else:
#         form = CardImageForm()
#     return render(request, "index.html", {'form': form})


# def upload(request):
#     if request.method == 'POST' and request.FILES['upload']:
#         upload = request.FILES['upload']
#         fss = FileSystemStorage()
#         file = fss.save(upload.name, upload)
#         file_url = fss.url(file)
#         print(file_url)
#         return render(request, 'user_card/index.html', {'file_url': file_url})
#     return render(request, 'user_card/index.html')

# def upload(request):
# 	if request.method == "POST":
# 		form = CardImageForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			form.save()
# 		return redirect("user_card:upload")
# 	cardimageform = CardImageForm()
# 	cardimage = CardImage.objects.all()
# 	return render(request=request, template_name="user_card/index.html", context={'form':cardimageform, 'cardimage':cardimage})


class CreateProfileView(CreateView):
    template_name = "user_card/index.html"
    model = CardImage
    fields = "__all__"
    success_url = "/emiratescard/upload"
