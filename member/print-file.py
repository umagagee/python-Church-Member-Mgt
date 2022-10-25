import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


def showPrint(request):
    buffer = io.BytesIO()

    p.canvas.Canvas(buffer)

    p.drawString(100,100,"Hello World")

    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer,as_attachment=True, filename="hello.pdf")

