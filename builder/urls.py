from django.urls import path
from . import views

urlpatterns = [
    # Home and Authentication
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('ats-scanner/<int:resume_id>/', views.ats_scanner, name='ats_scanner'),
    # Resume CRUD Operations
    path('resume/create/', views.create_resume, name='create_resume'),
    path('resume/edit/<int:pk>/', views.edit_resume, name='edit_resume'),
    path('resume/delete/<int:pk>/', views.delete_resume, name='delete_resume'),
    path('job-matcher/', views.job_matcher, name='job_matcher'),
    # AI and Parsing Features
    path('ai-suggest/', views.ai_suggest, name='ai_suggest'),
    path('upload-existing/', views.upload_existing_resume, name='upload_existing_resume'),
    path('ats-scanner/select/', views.ats_scanner_select, name='ats_scanner_select'),
    # Preview and Download
    path('resume/preview/<int:pk>/', views.preview_resume, name='preview_resume'),
    path('ats-scanner/upload/', views.ats_scanner_upload, name='ats_scanner_upload'),
    # KEY FIX: Changed 'download_resume_pdf' to 'download_resume'
    path('resume/download/<int:pk>/', views.download_resume_pdf, name='download_resume'),
    path('ats-scanner/upload/', views.ats_scanner_upload, name='ats_scanner_upload'),
]