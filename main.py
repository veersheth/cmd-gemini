from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-1.5-flash')

while True:
    prompt = input("Enter Prompt: ");
    
    if prompt == "":
        break

    response = model.generate_content(prompt)
    print(f"Gemini: {response.text}")