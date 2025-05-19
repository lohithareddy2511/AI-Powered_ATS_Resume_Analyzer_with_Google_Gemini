from dotenv import load_dotenv
import base64
import streamlit as st
import os
import io
from PIL import Image
import pdf2image
import google.generativeai as genai

# Configure API Key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set Poppler Path
poppler_path = r"C:\Program Files (x86)\poppler-24.08.0\Library\bin"  # Update this path

# Function to get response from Gemini AI
def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

# Function to process uploaded PDF
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        try:
            images = pdf2image.convert_from_bytes(uploaded_file.read(), poppler_path=poppler_path)
            first_page = images[0]

            img_byte_arr = io.BytesIO()
            first_page.save(img_byte_arr, format="JPEG")
            img_byte_arr = img_byte_arr.getvalue()

            pdf_parts = [
                {
                    "mime_type": "image/jpeg",
                    "data": base64.b64encode(img_byte_arr).decode(),
                }
            ]
            return pdf_parts
        except Exception as e:
            st.error(f"❌ Error processing PDF: {e}")
            return None
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit App Configuration
st.set_page_config(page_title="ATS Resume Expert", page_icon="📄", layout="wide")

# Custom CSS for Professional UI
st.markdown(
    """
    <style>
        body { background-color: #e3e6ea; } /* Professional light gray-blue */
        .main { background-color: #ffffff; padding: 20px; border-radius: 12px; }
        .stTextArea textarea {
            border-radius: 10px;
            border: 1px solid #007bff;
            padding: 10px;
        }
        .stFileUploader {
            padding: 10px;
            border-radius: 10px;
            background-color: #e3f2fd;
            border: 1px solid #007bff;
        }
        .response-card {
            padding: 20px;
            border-radius: 12px;
            background-color: #f4f4f4;
            margin-top: 10px;
            border-left: 5px solid #007bff;
        }
        .stButton>button {
            width: 100%;
            border-radius: 10px;
            font-size: 16px;
            padding: 10px;
            background-color: #007bff;
            color: white;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and Subtitle
st.markdown("<h1 style='text-align: center; color: #007bff;'>📑 ATS Resume Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: gray;'>Optimize Your Resume for Job Applications</h3>", unsafe_allow_html=True)

st.divider()

# Job Description Input
input_text = st.text_area("📋 Paste Job Description Here:", key="input", height=150)

# Resume Upload
uploaded_file = st.file_uploader("📂 Upload Your Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    st.success("✅ Resume uploaded successfully!")

# Buttons with columns for better spacing
col1, col2 = st.columns(2)
with col1:
    submit1 = st.button("📄 Analyze Resume")
with col2:
    submit3 = st.button("📊 Check Match Percentage")

# Enhanced Prompt for Resume Analysis
input_prompt1 = """
You are a highly experienced Technical Human Resource Manager with deep expertise in recruitment, talent acquisition, and ATS systems. 
Your role is to critically evaluate the provided resume against the given job description.

Your evaluation should be detailed and structured, covering the following aspects:

1️⃣ **Overall Fit** – Assess whether the candidate's skills, experience, and qualifications match the role.
2️⃣ **Key Strengths** – Identify strong points in the resume that align well with the job description.
3️⃣ **Major Weaknesses** – Highlight areas where the resume lacks key requirements.
4️⃣ **Missing Keywords & Skills** – Identify important job-related keywords or skills absent in the resume.
5️⃣ **Recommendations for Improvement** – Provide actionable suggestions on how the candidate can refine their resume to improve alignment.

⚠️ **Important:** 
- Only focus on objective, data-driven evaluation.
- Avoid generic responses—be specific in feedback.
- If the resume lacks crucial information, state it clearly.

Your response should be structured and formatted professionally for clear readability.
"""

# Enhanced Prompt for ATS Percentage Match
input_prompt3 = """
You are a highly advanced ATS (Applicant Tracking System) designed to analyze resumes with **maximum accuracy** based on industry best practices.

Your job is to analyze the resume against the provided job description and **provide an objective ATS score.**  
Your response must follow this **structured format**:

🔹 **Match Percentage:** _(Provide an exact percentage score from 0% to 100% indicating how well the resume aligns with the job description.)_

🔹 **Keyword Analysis:**  
   - ✅ **Matched Keywords:** List keywords found in both the resume and job description.
   - ❌ **Missing Keywords:** List crucial job-related terms missing from the resume.

🔹 **Skill Gap Analysis:**  
   - Highlight technical or soft skills required in the job description but missing in the resume.

🔹 **Final Recommendations:**  
   - Provide specific suggestions to improve the resume’s ATS score.
   - Advise on formatting, keyword inclusion, and any necessary content modifications.

⚠️ **Strict Guidelines:**  
- Do not provide vague responses—be precise and data-driven.  
- If the resume is missing crucial sections, clearly state what is missing.  
- Always give actionable insights based on **real-world hiring standards.**  
"""

# Resume Analysis
if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        if pdf_content:
            response = get_gemini_response(input_prompt1, pdf_content, input_text)
            st.markdown("<h3 style='color: #007bff;'>📋 Resume Analysis:</h3>", unsafe_allow_html=True)
            st.markdown(f"<div class='response-card'>{response}</div>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please upload the resume.")

# Percentage Match Analysis
elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        if pdf_content:
            response = get_gemini_response(input_prompt3, pdf_content, input_text)
            st.markdown("<h3 style='color: #007bff;'>📊 Match Percentage:</h3>", unsafe_allow_html=True)
            st.markdown(f"<div class='response-card'>{response}</div>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please upload the resume.")
