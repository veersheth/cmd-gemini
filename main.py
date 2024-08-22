from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-1.5-flash')

result = model.generate_content('hi what are you')
print(result.text)
# chat = model.start_chat(history=[])

# while True:
#     prompt = input("enter prompt: ")
#     response = chat.send_message(prompt)
# 

