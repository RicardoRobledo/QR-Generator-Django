from django.shortcuts import render
from qr_code.qrcode.utils import QRCodeOptions


def home(request):
    
    context = dict(
        my_options=QRCodeOptions(size='t', border=6, error_correction='L'),
    )
    
    return render(request, 'qr_generator/home.html', context=context)
