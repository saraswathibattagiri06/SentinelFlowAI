import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

try:
    client = genai.Client(api_key=api_key)
    # UPDATED MODEL NAME FOR 2026
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents="Explain SQL injection in one sentence."
    )
    print("✅ Gemini 2.5 is Working!")
    print(f"🤖 Response: {response.text}")
except Exception as e:
    print(f"❌ Gemini Failed: {e}")