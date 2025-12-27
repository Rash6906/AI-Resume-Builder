# 🧠 AI Resume Builder & ATS Auditor

An AI-powered web application built using **Django** and **Hugging Face (Llama 3)** that helps job seekers generate professional resumes, analyze ATS compatibility, and match resumes with job descriptions.

---

## 🚀 Project Highlights

- AI-generated resume content using Llama 3
- ATS compatibility auditing
- Resume-to-job matching with keyword analysis
- PDF & DOCX resume parsing
- Multiple professional resume templates
- Export resumes as clean, ready-to-submit PDFs

---

## 🌟 Features

### ✍️ AI Resume Writer
- Generates professional summaries and bullet points
- Powered by **Meta-Llama-3-8B-Instruct**
- Creates role-specific, impactful content

### 📊 ATS Compliance Scanner
- Checks resume structure and formatting
- Verifies presence of:
  - Summary
  - Skills
  - Experience
  - Education
  - Contact Information
- Improves resume readability for ATS systems

### 🎯 Job Matcher
- Compares resume with job description
- Provides:
  - Match percentage
  - Missing keywords
  - Skill alignment feedback

### 📄 Smart Resume Parsing
- Upload existing **PDF** or **DOCX** resumes
- Automatically extracts and populates resume data

### 🎨 Resume Templates
- ATS-Friendly
- Modern
- Classic
- Creative Elite

### 📥 PDF Export
- Generates clean, professional PDFs
- Uses `xhtml2pdf` for formatting

---

## 🛠️ Tech Stack

### Backend
- Django (Python)

### AI
- Hugging Face Inference API
- Meta-Llama-3-8B-Instruct

### Frontend
- Bootstrap 5
- Font Awesome
- JavaScript

### Resume Processing
- pdfplumber
- python-docx
- xhtml2pdf

### Security & Config
- python-dotenv

  AI-Resume-Builder/
│
├── builder/ # Resume builder app
├── templates/ # HTML templates
├── static/ # CSS, JS, images
├── media/ # Uploaded resumes
├── .env # Environment variables
├── requirements.txt
├── manage.py
└── README.md

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Rash6906/AI-Resume-Builder.git
cd AI-Resume-Builder
👩‍💻 Author

Rashmi P P
Aspiring Software Developer
GitHub: https://github.com/Rash6906

---

## 📂 Project Structure

