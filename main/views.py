from django.shortcuts import render, redirect
from django.http import HttpResponse
from rembg import remove
from PIL import Image
import io
import base64
import os

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def upload_image(request):
    if request.method == "POST":
        image_input = request.FILES["image"]

        input = Image.open(image_input)
        output = remove(input)
        output.save(f"{image_input}.png")

        output_buffer = io.BytesIO()
        output.save(output_buffer, format='PNG')
        output_buffer.seek(0)

        image_base64 = base64.b64encode(output_buffer.getvalue()).decode('utf-8')
        image_data_url = f"data:image/png;base64,{image_base64}"

        return render(request, "main/index.html", {
            "output_image": image_data_url,
            "original": image_input})

    return redirect("main:index")