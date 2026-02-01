from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import FileResponse
from rest_framework.permissions import IsAuthenticated
from .services.pdf_service import generate_pdf

from .models import Dataset
from .services.csv_service import process_csv


class UploadCSV(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        file = request.FILES.get("file")

        if not file:
            return Response(
                {"error": "No file uploaded"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            summary = process_csv(file)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

        Dataset.objects.create(
            file_name=file.name,
            summary=summary
        )

        if Dataset.objects.count() > 5:
            Dataset.objects.order_by("uploaded_at").first().delete()

        return Response(summary, status=status.HTTP_201_CREATED)


class DatasetHistory(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        datasets = Dataset.objects.order_by("-uploaded_at")[:5]

        return Response([
            {
                "file_name": d.file_name,
                "uploaded_at": d.uploaded_at,
                "summary": d.summary
            }
            for d in datasets
        ])
class GeneratePDFReport(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, dataset_id):
        try:
            dataset = Dataset.objects.get(id=dataset_id)
        except Dataset.DoesNotExist:
            return Response(
                {"error": "Dataset not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        pdf_path = generate_pdf(dataset)
        return FileResponse(open(pdf_path, "rb"), content_type="application/pdf")


class DatasetPDFReport(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, dataset_id):
        try:
            dataset = Dataset.objects.get(id=dataset_id)
        except Dataset.DoesNotExist:
            return Response(
                {"error": "Dataset not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        pdf_buffer = generate_pdf(dataset)

        return FileResponse(
            pdf_buffer,
            as_attachment=True,
            filename=f"report_{dataset.id}.pdf",
            content_type="application/pdf"
        )
