from django.shortcuts import render
from django.http import HttpResponse, FileResponse
import qrcode
import io
import os
from django.conf import settings
from datetime import datetime


def home(request):
    """
    Home page view - displays the form to generate QR codes
    """
    return render(request, 'generator/home.html')


def generate_qr(request):
    """
    Generate QR code based on user input and display it
    """
    if request.method == 'POST':
        # Get the data from the form
        data = request.POST.get('qr_data', '')
        
        if data:
            # Create QR code instance
            qr = qrcode.QRCode(
                version=1,  # controls the size of the QR code
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            
            # Add data to the QR code
            qr.add_data(data)
            qr.make(fit=True)
            
            # Create an image from the QR code
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Save the image temporarily
            # Create media directory if it doesn't exist
            media_dir = os.path.join(settings.MEDIA_ROOT, 'qrcodes')
            os.makedirs(media_dir, exist_ok=True)
            
            # Generate a unique filename with timestamp
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')
            filename = f'qrcode_{timestamp}.png'
            filepath = os.path.join(media_dir, filename)
            
            # Save the image
            img.save(filepath)
            
            # Create the URL for the image
            qr_code_url = f'{settings.MEDIA_URL}qrcodes/{filename}'
            
            context = {
                'qr_code_url': qr_code_url,
                'qr_data': data,
                'filename': filename,
            }
            
            return render(request, 'generator/result.html', context)
    
    # If not POST or no data, redirect to home
    return render(request, 'generator/home.html')


def download_qr(request):
    """
    Download the generated QR code
    """
    if request.method == 'GET':
        filename = request.GET.get('filename', '')
        
        if filename:
            filepath = os.path.join(settings.MEDIA_ROOT, 'qrcodes', filename)
            
            if os.path.exists(filepath):
                # Open the file and return it as a download
                response = FileResponse(open(filepath, 'rb'), content_type='image/png')
                response['Content-Disposition'] = f'attachment; filename="{filename}"'
                return response
    
    # If something went wrong, redirect to home
    return render(request, 'generator/home.html')
