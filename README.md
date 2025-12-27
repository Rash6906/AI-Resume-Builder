# AI Resume Builder & ATS Auditor

A professional, AI-driven web application built with **Django** and **Hugging Face (Llama 3)**. This tool empowers job seekers to generate high-quality resume content and audit their resumes for Applicant Tracking System (ATS) compatibility.

## 🌟 Key Features

* **AI Resume Writer:** Uses `Meta-Llama-3-8B-Instruct` via the Hugging Face Inference API to craft professional summaries and bullet points.
* **ATS Compliance Scanner:** Audits resumes for "robot-readability," checking for essential headers, contact information, and formatting.
* **Job Matcher:** Analyzes a resume against a specific job description to provide a matching score and identify missing keywords.
* **Smart Parsing:** Supports uploading existing PDF or DOCX files to automatically extract and populate data into the builder.
* **Dynamic Templates:** Offers multiple styles including ATS-friendly, Modern, Classic, and Creative Elite.
* **PDF Export:** Generates clean, formatted PDFs ready for submission using `xhtml2pdf`.

## 🛠️ Tech Stack

* **Framework:** Django (Python)
* **AI Integration:** Hugging Face Inference API (Llama 3)
* **Frontend:** Bootstrap 5, FontAwesome, JavaScript
* **Security:** `python-dotenv` for environment variable management
* **Libraries:** `pdfplumber`, `docx`, `xhtml2pdf`, `huggingface_hub`

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/Rash6906/AI-Resume-Builder.git](https://github.com/Rash6906/AI-Resume-Builder.git)
cd AI-Resume-Builder
