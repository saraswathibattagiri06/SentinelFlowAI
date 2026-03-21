import os
from google import genai

class ArchitectAgent:
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model_id = "gemini-2.5-flash"

    def generate_fix(self, bug_name, code):
        print(f"🏗️  Architect is fixing: {bug_name}...")
        prompt = f"Fix this {bug_name} vulnerability. Return ONLY the code, no markdown: \n{code}"
        
        try:
            response = self.client.models.generate_content(model=self.model_id, contents=prompt)
            return response.text.strip()
        except Exception as e:
            print(f"❌ Gemini Error: {e}")
            return None

    def save_patch(self, filename, fixed_code):
        os.makedirs("patches", exist_ok=True)
        path = f"patches/fixed_{os.path.basename(filename)}"
        with open(path, "w") as f:
            f.write(fixed_code)
        return path