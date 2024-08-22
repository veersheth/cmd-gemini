import os
import logging
import argparse
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

logging.basicConfig(filename='chat.log', level=logging.INFO, format='%(asctime)s - %(message)s')

parser = argparse.ArgumentParser(description='Chat with Gemini AI')
parser.add_argument('--api_key', type=str, help='API key for Gemini AI')
args = parser.parse_args()

api_key = args.api_key or os.getenv("GEMINI_API_KEY")

if not api_key:
    print("no api key passed or in environment")
    exit()

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

# main loop
while True:
    prompt = input("Enter Prompt: ")
    
    if prompt == "":
        break

    try:
        response = chat.send_message(prompt)
        print(f"Gemini: {response.text}")
        logging.info(f"User: {prompt} | Gemini: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
        logging.error(f"Error: {e}")