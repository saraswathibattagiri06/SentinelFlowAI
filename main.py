import os
from agents.scout.agent import ScoutAgent
from agents.architect.agent import ArchitectAgent

def run_sentinelflow():
    print("🚀 Starting SentinelFlow AI Security Loop...")
    
    scout = ScoutAgent()
    architect = ArchitectAgent()

    # 1. Get findings from the Scout
    findings = scout.get_vulnerabilities()

    if not findings:
        print("🎉 No vulnerabilities to fix today!")
        return

    # 2. Process each finding with the Architect
    for bug in findings:
        print(f"🛠️  Processing: {bug['name']}")
        
        # Architect writes the fix using Gemini
        fix = architect.generate_fix(bug['name'], bug['code_context'])
        
        if fix:
            # Save the fixed version to the patches/ folder
            architect.save_patch(bug['file'], fix)

if __name__ == "__main__":
    run_sentinelflow()