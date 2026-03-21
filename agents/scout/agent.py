import gitlab
import os
from dotenv import load_dotenv

load_dotenv() # This loads the variables from your .env file

class ScoutAgent:
    def __init__(self):
        self.gl = gitlab.Gitlab('https://gitlab.com', private_token=os.getenv('GITLAB_TOKEN'))
        self.project = self.gl.projects.get(os.getenv('PROJECT_ID'))

    def find_vulnerabilities(self):
        # Fetch the latest SAST/DAST findings
        vulnerabilities = self.project.vulnerabilities.list()
        # Filter for Critical/High that haven't been dismissed
        return [v for v in vulnerabilities if v.severity in ['critical', 'high'] and v.state == 'detected']

# Mock execution for the hackathon
if __name__ == "__main__":
    scout = ScoutAgent()
    print(f"Scout found {len(scout.find_vulnerabilities())} high-risk targets.")