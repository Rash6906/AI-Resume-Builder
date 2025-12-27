
import requests
import io
from pdfminer.high_level import extract_text
import docx

def extract_text_from_pdf(pdf_file):
    return extract_text(io.BytesIO(pdf_file.read()))

def extract_text_from_docx(docx_file):
    doc = docx.Document(io.BytesIO(docx_file.read()))
    return "\n".join([para.text for para in doc.paragraphs])

def simple_resume_parser(text):
    """
    A simple logic to find common fields. 
    In a real app, you might use AI (LLMs) or Regex here.
    """
    lines = text.split('\n')
    extracted_data = {
        'full_name': lines[0] if lines else "",
        'objective': text[:500], # Grab the first 500 chars as a start
    }
    # Logic to find Email/Phone via Regex would go here
    return extracted_data

def parse_resume_with_hf(raw_text, api_key):
    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    # We create a prompt that forces the AI to give us JSON
    prompt = f"""
    Extract the following entities from the resume text below: 
    Full Name, Email, Phone, Objective, Skills (comma separated), Education (List of school and degree).
    Return ONLY a JSON object.
    
    Resume Text: {raw_text[:2000]} 
    """

    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    
    if response.status_code == 200:
        # Note: You may need to clean the response string to extract the JSON part
        return response.json() 
    return None