import openai
import os
import pandas as pd
import PyPDF2

# Set your OpenAI API key
openai.api_key = "your-api-key"

class Chatbot:
    def __init__(self):
        self.context = ""

    def process_file(self, uploaded_file):
        """Process uploaded file and extract text."""
        file_type = uploaded_file.type

        if file_type == "application/pdf":
            self.context = self.extract_text_from_pdf(uploaded_file)
        elif file_type == "text/plain":
            self.context = uploaded_file.read().decode("utf-8")
        elif file_type == "text/csv":
            df = pd.read_csv(uploaded_file)
            self.context = df.to_string()

    def extract_text_from_pdf(self, pdf_file):
        """Extract text from a PDF file."""
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text

    def get_response(self, user_input):
        """Generate a response using OpenAI GPT-4 model."""
        prompt = f"Context: {self.context}\nUser: {user_input}\nAI:"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are an AI assistant."},
                      {"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
