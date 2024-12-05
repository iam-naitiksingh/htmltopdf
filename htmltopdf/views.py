from django.shortcuts import render
from django.http import HttpResponse
from weasyprint import HTML
import os

def generatepdf(request):
    try:
        if request.method == "POST" and request.FILES['html_file']:
            uploaded_file = request.FILES['html_file']

            # Read the uploaded HTML file content
            html_content = uploaded_file.read().decode('utf-8')

            # Generate PDF from the uploaded HTML content
            response = HttpResponse(content_type="application/pdf")
            response['Content-Disposition'] = 'attachment; filename="generated_pdf.pdf"'

            # Convert HTML to PDF
            html = HTML(string=html_content)
            html.write_pdf(response)

            return response
        else:
            return HttpResponse("No file uploaded or invalid request.", status=400)

    except Exception as e:
        return HttpResponse(f"Error: {e}", status=500)

def testpdf(request):
    return render(request, 'test_pdf.html')
