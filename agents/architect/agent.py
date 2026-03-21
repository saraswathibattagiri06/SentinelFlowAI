import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

class ArchitectAgent:
    def __init__(self):
        # Using the model that worked in your test!
        self.client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model_id = "gemini-2.5-flash"

    def generate_fix(self, vulnerability_name, code_context):
        print(f"🏗️  Architect is designing a fix for: {vulnerability_name}...")
        
        prompt = f"""
        You are an expert Security Engineer. 
        A vulnerability has been detected in the following code:
        
        Vulnerability: {vulnerability_name}
        Original Code:
        {code_context}
        
        Your task:
        1. Fix the vulnerability while maintaining the original functionality.
        2. Follow secure coding best practices.
        3. Return ONLY the corrected code block. No explanations, no markdown backticks.
        """

        try:
            response = self.client.models.generate_content(
                model=self.model_id, 
                contents=prompt
            )
            return response.text.strip()
        except Exception as e:
            print(f"❌ Architect Failed to generate fix: {e}")
            return None

    def save_patch(self, filename, fixed_code):
        os.makedirs("patches", exist_ok=True)
        # We save it as a .patch or a fixed version of the file
        patch_path = f"patches/fixed_{os.path.basename(filename)}"
        with open(patch_path, "w") as f:
            f.write(fixed_code)
        print(f"💾 Patch saved to: {patch_path}")
        return patch_path

if __name__ == "__main__":
    # Quick test logic
    architect = ArchitectAgent()
    # Mock finding for testing
    sample_code = "query = 'SELECT * FROM users WHERE id = ' + user_id"
    fix = architect.generate_fix("SQL Injection", sample_code)
    if fix:
        architect.save_patch("database.py", fix)