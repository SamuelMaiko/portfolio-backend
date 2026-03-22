import os
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from .models import SaccoAppUpdate

def download_apk(request, version_name):
    """
    Download view for APK files using version_name.
    """
    update = get_object_or_404(SaccoAppUpdate, version_name=version_name)
    if not update.apk_file or not os.path.exists(update.apk_file.path):
        raise Http404("APK file not found on server storage.")
        
    filename = f"sacco-app-v{update.version_name}.apk"
    response = FileResponse(update.apk_file.open('rb'), content_type='application/vnd.android.package-archive')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response
