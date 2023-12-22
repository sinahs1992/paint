from django.shortcuts import render, redirect
from .models import Files, Drawing
from django.http import HttpResponseRedirect

def index(request):
    if request.method == 'GET':
        return render(request, 'paintapp/index.html')
    elif request.method == 'POST':
        print(request.POST)
        return HttpResponseRedirect('/')
        # filename = request.POST['save_fname']
        # data = request.POST['save_cdata']
        # image = request.POST['save_image']
        # file_data = Files(name=filename, image=data, canvas_image=image)
        # file_data.save()
        # return HttpResponseRedirect('/')



def index(request):
    if request.method == 'POST':
        # Handle saving the drawing
        image_data = request.POST.get('image_data')  # Assuming you send the image data via POST
        Drawing.objects.create(image=image_data)
        return redirect('paintapp:index')

    drawings = Drawing.objects.all()
    return render(request, 'paintapp/index.html', {'drawings': drawings})

def drawing_list(request):
    drawings = Drawing.objects.all()
    return render(request, 'paintapp/show.html', {'drawings': drawings})