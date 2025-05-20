from django.http import FileResponse, Http404
from .models import Document

def install_file(request):
    try:
        document = Document.objects.last()  # или любой фильтр
        return FileResponse(document.file.open(), as_attachment=True, filename=document.file.name)
    except Document.DoesNotExist:
        raise Http404("Документ не найден")
