import os
import sys
from dotenv import load_dotenv
load_dotenv()

# Crucial: Fixes the 'ModuleNotFound' squiggles
base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(base_dir, 'agents'))

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

    # 📝 Final Report Generation
    with open("gl-job-summary.md", "w", encoding="utf-8") as f:
        f.write("# 🛡️ SentinelFlow AI Remediation Report\n")
        f.write(f"**Total Patches Generated:** {fixed_count}\n\n")
        f.write("| Vulnerability | File | Status |\n| :--- | :--- | :--- |\n")
        for bug in findings:
            f.write(f"| {bug['name']} | `{bug['file']}` | ✅ Remediation Ready |\n")
            
    print(f"✨ Success! {fixed_count} patches generated in /patches")

if __name__ == "__main__":
    run_sentinelflow()