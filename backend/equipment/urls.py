from django.urls import path
from .views import UploadCSV, DatasetHistory, DatasetPDFReport

urlpatterns = [
    path("upload/", UploadCSV.as_view()),
    path("history/", DatasetHistory.as_view()),
    path("report/<int:dataset_id>/", DatasetPDFReport.as_view()),
]


