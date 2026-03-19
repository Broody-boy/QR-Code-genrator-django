from django.shortcuts import render
from django.http import HttpResponse
import qrcode
import io
import base64


def home(request):
    return render(request, 'generator/home.html')


def _make_qr_image(data):
    """Generate QR code and return as PNG bytes."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    return buffer.read()


def generate_qr(request):
    if request.method == 'POST':
        data = request.POST.get('qr_data', '')
        if data:
            png_bytes = _make_qr_image(data)
            b64 = base64.b64encode(png_bytes).decode('utf-8')
            context = {
                'qr_code_url': f'data:image/png;base64,{b64}',
                'qr_data': data,
                # pass data encoded for use in download URL
                'qr_data_b64': base64.urlsafe_b64encode(data.encode()).decode(),
            }
            return render(request, 'generator/result.html', context)
    return render(request, 'generator/home.html')


def download_qr(request):
    data_b64 = request.GET.get('data', '')
    if data_b64:
        try:
            data = base64.urlsafe_b64decode(data_b64.encode()).decode()
            png_bytes = _make_qr_image(data)
            response = HttpResponse(png_bytes, content_type='image/png')
            response['Content-Disposition'] = 'attachment; filename="qrcode.png"'
            return response
        except Exception:
            pass
    return render(request, 'generator/home.html')
