import os
import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyDBtGk8ZgX3_S7zjZH3-ywMitCwJy7sSn0"
# GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
# Use the correct model name (Gemini 1.5 Flash)
model = genai.GenerativeModel('gemini-1.5-flash')  # Updated to Flash model

def get_chat_response(user_input, chat_history=None):
    try:
        if chat_history is None:
            chat_history = []
        
        chat = model.start_chat(history=chat_history)
        response = chat.send_message(user_input)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"