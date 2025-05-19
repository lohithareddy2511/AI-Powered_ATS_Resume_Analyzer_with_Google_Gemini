# AI-Powered_ATS_Resume_Analyzer_with_Google_Gemini

A smart **AI-powered web app** built with **Streamlit** and **Google Gemini AI** that helps job seekers evaluate and optimize their resumes based on job descriptions. Designed to simulate an **Applicant Tracking System (ATS)** and a **human recruiter**, the app provides in-depth resume analysis and calculates a match percentage score.

## 🔍 Features

* ✅ **Resume Upload & Parsing**: Upload your PDF resume and get it analyzed instantly.
* 🧠 **AI-Powered Resume Evaluation**: Leverages Gemini AI to simulate a professional HR expert’s detailed review.
* 📊 **ATS Match Score**: Calculates a percentage match between your resume and job description based on keywords, skills, and relevance.
* 📌 **Actionable Feedback**: Receive specific, structured suggestions to enhance your resume.
* 🎯 **Professional UI**: Clean and intuitive Streamlit interface with custom styling for enhanced user experience.

## 🛠️ Tech Stack

| Technology         | Description                         |
| ------------------ | ----------------------------------- |
| `Streamlit`        | Frontend Web UI framework           |
| `Google Gemini AI` | LLM used for resume analysis        |
| `pdf2image`        | Converts PDF resume to image        |
| `Pillow (PIL)`     | Image processing                    |
| `dotenv`           | Environment variable management     |
| `base64`           | PDF image encoding for Gemini input |

## 📦 Installation

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/ats-resume-analyzer.git
cd ats-resume-analyzer
```

2. **Create and Activate a Virtual Environment** (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Set Up Environment Variable**

Create a `.env` file in the root directory and add your Google API Key:

```env
GOOGLE_API_KEY=your_google_generative_ai_key
```

> 💡 You need access to the **Gemini API** from Google. You can get your API key from [Google AI Studio](https://aistudio.google.com/).

5. **Set Poppler Path (Windows Only)**

Download [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/), extract it, and update the path in the script:

```python
poppler_path = r"C:\Program Files (x86)\poppler-24.08.0\Library\bin"
```

## 🚀 Running the App

```bash
streamlit run your_app.py
```

> Replace `your_app.py` with the actual filename if different.

## 📂 File Structure

```bash
ats-resume-analyzer/
│
├── .env                     # Environment variable for API key
├── app.py                   # Main Streamlit application
├── requirements.txt         # Python dependencies
└── README.md                # GitHub documentation
```

## 🧪 How It Works

1. **Input**: Paste a job description and upload a PDF resume.
2. **Processing**: Resume is converted to an image (first page) and sent to Gemini AI along with the job description and predefined prompts.
3. **AI Analysis**:

   * One mode simulates a **human recruiter** giving a professional critique.
   * Another mode simulates an **ATS system** scoring the resume objectively.
4. **Output**: Structured, clear, and useful feedback is displayed in the app.

## 📸 Results
