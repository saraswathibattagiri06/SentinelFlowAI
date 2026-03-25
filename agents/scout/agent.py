import os
import gitlab

class ScoutAgent:
    def __init__(self):
        self.gl = gitlab.Gitlab('https://gitlab.com', private_token=os.getenv('GITLAB_TOKEN'))
        self.project_id = os.getenv('PROJECT_ID')
        self.project = self.gl.projects.get(self.project_id)

    def get_vulnerabilities(self):
        print(f"🔍 Scout is scanning project: {self.project.name}...")
        
        findings = []
        try:
           
            vulnerabilities = self.project.vulnerabilities.list(state='detected', severity=['critical', 'high'])
            for v in vulnerabilities:
                findings.append({
                    "name": v.name,
                    "file": v.location.get('file', 'app.py'),
                    "code_context": self._fetch_file(v.location.get('file'))
                })
        except Exception:
      
            print("⚠️ GitLab Security API restricted. Entering Demo Mode...")
            findings.append({
                "name": "SQL Injection",
                "file": "database.py",
                "code_context": "def get_user(id):\n    return db.execute('SELECT * FROM users WHERE id = ' + id)"
            })
            
        return findings

    def _fetch_file(self, path):
        try:
            return self.project.files.get(file=path, ref='main').decode().decode('utf-8')
        except:
            return "# Code context unavailable"