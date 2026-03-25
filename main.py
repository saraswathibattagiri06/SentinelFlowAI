import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()

base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(base_dir, 'agents'))
model = genai.GenerativeModel('gemini-3-flash')
from agents.scout.agent import ScoutAgent
from agents.architect.agent import ArchitectAgent

def run_sentinelflow():
    print("🚀 SentinelFlow AI: Initiating Secure Pipeline...")
    
    scout = ScoutAgent()
    architect = ArchitectAgent()
    findings = scout.get_vulnerabilities()

    if not findings:
        print("✅ No issues found.")
        return

    fixed_count = 0
    for bug in findings:
        fix = architect.generate_fix(bug['name'], bug['code_context'])
        if fix:
            architect.save_patch(bug['file'], fix)
            fixed_count += 1
# Sustainability Optimization: 
# We use Gemini 3 Flash to reduce computational overhead.
# We set max_output_tokens to 1024 to prevent 'token wandering' and save energy.

def get_efficient_response(prompt):
    response = model.generate_content(
        prompt,
        generation_config={
            "max_output_tokens": 1024,
            "temperature": 0.2, # Lower temperature for more direct, energy-efficient answers
        }
    )
    return response

    with open("gl-job-summary.md", "w", encoding="utf-8") as f:
        f.write("# 🛡️ SentinelFlow AI Remediation Report\n")
        f.write(f"**Total Patches Generated:** {fixed_count}\n\n")
        f.write("| Vulnerability | File | Status |\n| :--- | :--- | :--- |\n")
        for bug in findings:
            f.write(f"| {bug['name']} | `{bug['file']}` | ✅ Remediation Ready |\n")
            
    print(f"✨ Success! {fixed_count} patches generated in /patches")

if __name__ == "__main__":
    run_sentinelflow()