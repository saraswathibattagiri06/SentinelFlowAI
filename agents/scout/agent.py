import os
import gitlab
from dotenv import load_dotenv

load_dotenv()

class ScoutAgent:
    def __init__(self):
        self.gl = gitlab.Gitlab('https://gitlab.com', private_token=os.getenv('GITLAB_TOKEN'))
        self.project_id = os.getenv('PROJECT_ID')
        self.project = self.gl.projects.get(self.project_id)

    
    def get_vulnerabilities(self):
        print(f"🔍 Scout is scanning project: {self.project.name}...")
        
        # Get detected vulnerabilities
        vulnerabilities = self.project.vulnerabilities.list(
            state='detected', 
            severity=['critical', 'high']
        )
        
        findings = []
        for v in vulnerabilities:
            # We extract the file path and line number for the Architect
            file_path = v.location.get('file')
            line_num = v.location.get('start_line')
            
            # 💡 PRO TIP: Fetch the actual source code around the bug
            try:
                f = self.project.files.get(file=file_path, ref='main')
                content = f.decode().decode('utf-8')
                # Send the specific context to the Architect
                findings.append({
                    "id": v.id,
                    "name": v.name,
                    "file": file_path,
                    "line": line_num,
                    "code_context": content
                })
                print(f"⚠️ FOUND: {v.name} in {file_path}")
            except:
                print(f"⚠️ Could not fetch source for {v.name}")

        return findings

if __name__ == "__main__":
    scout = ScoutAgent()
    scout.get_vulnerabilities()